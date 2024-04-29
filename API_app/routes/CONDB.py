from typing import Optional
from fastapi import APIRouter, Depends

from API_app.model.dataclass import DataInput, PredictOutput

from sqlalchemy.orm import Session
from DW.DB.async_connection import get_db, get_items
from DW.DB.db_models.base_model import Test_Table
from API_app.apis import test # main logic

CONDB = APIRouter(
    prefix="/conDB", # url 앞에 고정적으로 붙는 prefix path 추가
) # root에서 분리된 경로

@CONDB.get("/") # Route Path
def test_index(db: Session = Depends(get_db)):
	res = test.test_index(db=db) # apis 호출
	return {"res" : res,} # 결과

@CONDB.get("/read")
def read_Item(db:Session=Depends(get_db)):
    return get_items(db) #db.query(test_model.Test_Table).all()

@CONDB.post("/post")
def create_Item(Input:DataInput,db:Session=Depends(get_db)):
    DB_Table = Test_Table()
    db.add(DB_Table)
    db.commit()
    return Input

# @conDB.put("/")
# def update_Item

# @conDB.delete("/")
# def delete_Item():
    