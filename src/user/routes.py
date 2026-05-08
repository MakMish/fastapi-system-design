from fastapi import APIRouter,Depends,UploadFile,File,Form
import logging
from src.user.ai import aiit
from src.tasks import asre
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordRequestForm
from src.user.model import urespmode
from src.user.model import data,deta2
from src.utils.dbconn import get_db
from src.cloud import img
from pydantic import EmailStr
from datetime import datetime,timedelta
from src.user.user_auth import verify_acc_token
from sqlalchemy.ext.asyncio import AsyncSession
from src.user.services import all_data,add_data,login
def data1():
    return datetime.utcnow()
router=APIRouter(prefix="/user")
logger=logging.getLogger(__name__)
@router.get("/all",response_model=list[urespmode])
async def getall(db:AsyncSession=Depends(get_db)):
    logger.info("all called")
    return await all_data(db)

@router.post("/login")
async def login1(request1:Request,deta:OAuth2PasswordRequestForm=Depends(),dba:AsyncSession=Depends(get_db)):
    logger.info("login called")
    return await login(request=request1,data=deta,db1=dba)

@router.post("/register")
async def signin(request1:Request,deta:data,dba:AsyncSession=Depends(get_db)):
    logger.info("register called")
    return await add_data(request=request1,data1=deta,db=dba)

@router.post("/img_url")
async def upld(request1:Request,file2:UploadFile=File(...)):
    return await img(request=request1,file1=file2)

@router.post("/verify_acc_tok")
async def acc_ver(acc_tok1:str):
    return await verify_acc_token(acc_tok=acc_tok1)

@router.post("/ask")
async def askit(request1:Request,data:deta2):
    return await aiit(request=request1,task=data.query)

@router.post("/try")
def ash(Email:EmailStr=Form(...)):
    asre.apply_async(args=[Email],eta=data1()+timedelta(minutes=2))
    return{
        "status":"success"
    }