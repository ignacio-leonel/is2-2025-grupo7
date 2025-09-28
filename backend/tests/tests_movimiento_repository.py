



import pytest
from datetime import datetime
from backend.repositories.movimiento_repository import MovimientoRepository


@pytest.fixture
def fake_db_session():
    
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine("sqlite:///:memory:")
    Session = sessionmaker(bind = engine)
    
    yield Session()

@pytest.fixture
def test_crear_movimiento_valido(fake_db_session):
    repo = MovimientoRepository(Session = fake_db_session)
    movimiento_data = {
        "producto_id": 1,
        "cantidad": 10,
        "tipo": "entrada"
        }
    movimiento = repo.crear_movimiento(movimiento_data)
    assert movimiento.id is not None
    assert movimiento.cantidad == 10
    assert movimiento.tipo == "entrada"
    assert hasattr(movimiento, fecha_creacion)
    
def test_crear_movimiento_salida_sin_stock(fake_db_session):
    repo = MovimientoRepository(Session = fake_db_session)
    
    with pytest.raises(ValueError):
        repo.crear_movimiento(producto_id = 2, cantidad = 5, tipo = "salida")