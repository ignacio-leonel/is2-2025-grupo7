# module: backend/app/db/models/movimiento.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, CheckConstraint, text
from sqlalchemy.orm import relationship
from backend.app.domain.models.movimiento import TipoMovimiento
from backend.app.db.base import base # clase de la base de dato de SQLAlchemy

class MovimientoORM(base):
    __tablename__ = "movimientos"
    __table_args__ = (
        CheckConstraint('cantidad >= 0', name='ck_movimientos_cantidad_non_negative'),
    )
    # Columnas de la tabla
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False, index=True)
    deposito_origen_id = Column(Integer, ForeignKey("depositos.id"), nullable=True, index=True)
    deposito_destino_id = Column(Integer, ForeignKey("depositos.id"), nullable=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False, index=True)
    cantidad = Column(Integer, nullable=False)
    # Fecha la asigna la base de datos para evitar desincronías de horario
    fecha = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), nullable=False)
    tipo = Column(Enum(TipoMovimiento, native_enum=False), nullable=False)  # como string en BD

    # Relaciones
    producto = relationship("ProductoORM", back_populates="movimientos")
    deposito_origen = relationship("DepositoORM",foreign_keys=[deposito_origen_id],back_populates="movimientos_origen")
    deposito_destino = relationship("DepositoORM",foreign_keys=[deposito_destino_id],back_populates="movimientos_destino")
    usuario = relationship("UsuarioORM")

    # Representación para debugging
    def __repr__(self):
        return (
            f"<MovimientoORM(id={self.id}, producto_id={self.producto_id}, "
            f"deposito_origen_id={self.deposito_origen_id}, deposito_destino_id={self.deposito_destino_id}, "
            f"usuario_id={self.usuario_id}, cantidad={self.cantidad}, fecha={self.fecha}, tipo={self.tipo})>"
        )