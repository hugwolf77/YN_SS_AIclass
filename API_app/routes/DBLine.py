from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from DW.db.connection import get_db
from DW.db.crud import crud_test
from apis import test # main logic


router = APIRouter(
    prefix="/DBLine", # url 앞에 고정적으로 붙는 prefix path 추가
) # root에서 분리된 경로

@router.get("/DataLine") # Route Path
def test_index(db: Session = Depends(get_db)):
	
	res = test.test_index(db=db) # apis 호출
	
	return {
        "res" : res,
	} # 결과