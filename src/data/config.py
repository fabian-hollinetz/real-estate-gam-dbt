from sqlalchemy import create_engine

def get_engine():
    """
    Returns a SQLAlchemy engine to connect to the Postgres database.
    """
    engine = create_engine(
        "postgresql://dbt_user:dbt123@localhost:5432/realestate"
    )
    return engine
