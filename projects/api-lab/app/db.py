from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://lab_admin:j0s3l3@host.docker.internal:5432/lab_db"

engine = create_engine(DATABASE_URL)

def test_connection():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        return str(result.fetchone())