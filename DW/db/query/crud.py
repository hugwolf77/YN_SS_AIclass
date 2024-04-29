from sqlalchemy.orm import Session
from DW.DB.db_models.base_model import Base

def get_items(db: Session):
    return db.query(Base).all()