from src.utils.dbconn import Base
from sqlalchemy import Column,Integer,VARCHAR,Date
from datetime import datetime
def dateaajki():
   return datetime.now().date
class impexp(Base):
    __tablename__="user_table_syst"
    id=Column(Integer,autoincrement=True,primary_key=True)
    Name=Column(VARCHAR(30),unique=True,nullable=False)
    email=Column(VARCHAR(30),unique=True,nullable=False)
    hash_password=Column(VARCHAR(500),nullable=False,unique=True)
    reftok=Column(VARCHAR(500),unique=True,nullable=False)
    dateofopen=Column(Date,default=dateaajki())
    img_url=Column(VARCHAR(500),default="https://img.freepik.com/free-photo/happines-cheerful-perforated-paper-smiley-face_53876-14247.jpg?semt=ais_hybrid&w=740&q=80")