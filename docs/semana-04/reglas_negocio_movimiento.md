Reglas de negocio para MovimientoRepository

1. Crear movimiento:
   - 'cantidad' debe ser > 0
   - 'tipo' puede ser 'entrada' o 'salida'
   - Si es 'salida', verificar que el stock sea suficiente
   - Guardar fecha/hora UTC de creación

2. Actualizar movimiento:
   - No se puede cambiar producto_id
   - Si se modifica cantidad, actualizar stock y registro de auditoría

3. Eliminar movimiento:
   - Solo eliminación lógica (activo = False)
