from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from DW.db.connection import get_db
from DW.db.crud import crud_test
from DW.db.db_models import test_model
from apis import test # main logic


conDB = APIRouter(
    prefix="/conDB", # url 앞에 고정적으로 붙는 prefix path 추가
) # root에서 분리된 경로

@conDB.get("/") # Route Path
def test_index(db: Session = Depends(get_db)):
	res = test.test_index(db=db) # apis 호출
	return {"res" : res,} # 결과

@conDB.get("/read")
def read_Item(db:Session=Depends(get_db)):
    return crud_test.get_items(db) #db.query(test_model.Test_Table).all()

@conDB.post("/post")
def create_Item()