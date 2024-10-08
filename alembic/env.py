from logging.config import fileConfig
import os
from urllib.parse import quote_plus
from backend.models import Base
from dotenv import load_dotenv
from sqlalchemy import create_engine, engine_from_config
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    load_dotenv()

    password = os.getenv("SUPABASE_DB_PASSWORD")
    # URL-encode the password to handle special characters
    encoded_password = quote_plus(password)
    # Database connection string
    DATABASE_URL = f"postgresql+psycopg2://postgres.swepuhgtuviijqvdptmp:{encoded_password}@aws-0-us-east-1.pooler.supabase.com:6543/postgres"
    connectable = create_engine(DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=Base.metadata  # Provide the metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
