from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Este es el objeto de configuración de Alembic,
# que nos da acceso a los valores del archivo .ini en uso.
config = context.config

# Interpretar el archivo de configuración para logging.
# Básicamente configura los loggers.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Agregar el objeto MetaData de tus modelos
# para que 'autogenerate' funcione
from backend.app.db.base import Base
from backend.app.db.models import producto  # importa tu archivo producto.py

target_metadata = Base.metadata
