from sqlalchemy.orm import Session
from DW.DB.db_models.base_model import Test_Table

def get_items(db: Session):
    return db.query(Test_Table).all()