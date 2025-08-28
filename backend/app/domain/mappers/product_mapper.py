from app.db.models.producto import ProductORM
from app.domain.models.producto import Producto


def productORM_to_domain(orm_obj: ProductORM)-> Producto:
    return Producto(
        id= orm_obj.id,
        nombre= orm_obj.nombre,
        sku= orm_obj.SKU,
        descripcion= orm_obj.descripcion,
    )


def productDom_to_orm(dom_object: Producto) -> ProductORM:
    return ProductORM(
        id= dom_object.id,
        nombre= dom_object.nombre,
        SKU=dom_object.sku,
        categoria= dom_object.categoria,
        descripcion= dom_object.descripcion,
        unidad_medida= dom_object.stock_global
    )