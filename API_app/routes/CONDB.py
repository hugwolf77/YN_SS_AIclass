import logging
from typing import Optional
from fastapi import APIRouter, Depends
from API_app.model.dataclass import DataInput, PredictOutput
from sqlalchemy.orm import Session
from DW.DB.async_connection import get_db_session
from DW.DB.db_models.base_model import Base
from API_app.apis import test # main logic

logger = logging.getLogger("CONDB")
CONDB = APIRouter(prefix="/conDB",) 

@CONDB.get("/")
def test_index(db: Session = Depends(get_db_session)):
    res = test.test_index(db=db)
    logger.info("Client got test response {}, by use session :{}".format(res, db))
    return {"res" : res,}

@CONDB.get("/read")
def read_Item(db:Session=Depends(get_db_session)):
    return db.query(Base).all()

@CONDB.post("/post")
def create_Item(Input:DataInput,db:Session=Depends(get_db_session)):
    DB_Table = Base()
    db.add(DB_Table)
    db.commit()
    return Input

# @conDB.put("/")
# def update_Item

# @conDB.delete("/")
# def delete_Item():
    