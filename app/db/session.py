from app.db.database import Database
from app.core.config import settings
from app.db.base import Base

from app.db.models import user, vehicles

target_metadata = Base.metadata

db = Database(settings.DATABASE_URL)

def get_db():
    session = db.get_session()
    try:
        yield session
    finally:
        session.close()
