from app.db.database import Database
from app.core.config import DB_URL

db = Database(DB_URL)

def get_db():
    session = db.get_session()
    try:
        yield session
    finally:
        session.close()
