# import sys
# sys.path.append("D:/2024/Finance/NABI/NABI/core")

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base # Base 생성
from dotenv import load_dotenv
from core.config import Settings

configs = Settings()

# load_dotenv(dotenv_path="./core/.env",verbose=True)
# SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')
SQLALCHEMY_DATABASE_URL = configs.DATABASE_URL 
# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
engine = create_engine(SQLALCHEMY_DATABASE_URL) # fast_executemany=True 사용가능 확인
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

def conn_db():
    db_conn = engine
    return db_conn

def get_db():
	db = SessionLocal()
	try:
		yield db # DB 연결 성공한 경우, DB 세션 시작
	finally:
		db.close()
		# db 세션이 시작된 후, API 호출이 마무리되면 DB 세션을 닫아준다.


# if __name__=="__main__":
#    db = get_db()  