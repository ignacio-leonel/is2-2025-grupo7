from typing import Optional
from backend.app.domain.models.movimiento import Movimiento, TipoMovimiento
from backend.app.domain.models.producto import Producto
from backend.app.domain.models.deposito import Deposito
from backend.app.domain.models.usuario import Usuario
from backend.app.db.models.movimiento import MovimientoORM

#Convierte un MovimientoORM a Movimiento del dominio
def movimiento_orm_to_domain(
    orm: MovimientoORM,
    producto: Producto,
    usuario: Usuario,
    deposito_origen: Optional[Deposito] = None,
    deposito_destino: Optional[Deposito] = None
) -> Movimiento:
    return Movimiento(
        id=orm.id,
        producto=producto,
        deposito_origen=deposito_origen,
        deposito_destino=deposito_destino,
        usuario=usuario,
        cantidad=orm.cantidad,
        fecha=orm.fecha,
        tipo=TipoMovimiento(orm.tipo)
    )

#Convierte un Movimiento del dominio a MovimientoORM listo para persistencia
def movimiento_domain_to_orm(domain: Movimiento) -> MovimientoORM:
    orm = MovimientoORM(
        producto_id=domain.producto.id,
        deposito_origen_id=domain.deposito_origen.id if domain.deposito_origen else None,
        deposito_destino_id=domain.deposito_destino.id if domain.deposito_destino else None,
        usuario_id=domain.usuario.id,
        cantidad=domain.cantidad,
        fecha=domain.fecha,
        tipo=domain.tipo.value
    )
    if domain.id is not None:
        orm.id = domain.id
    return orm