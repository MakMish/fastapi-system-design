from jose import jwt,JWTError
from fastapi.responses import JSONResponse
import redis
from src.dbmodel import Setting
from  datetime import datetime,timedelta
from sqlalchemy import select
from src.user.schema import impexp
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.utils.dbconn import get_db
r=redis.from_url(Setting().redis_url)
async def create_refresh_token(dict_data:dict):
    try:
        encode=dict_data.copy()
        exp=datetime.utcnow()+timedelta(days=7)
        encode.update({"exp":exp})
        token=jwt.encode(encode,Setting().SECRET_KEY,algorithm=Setting().ALGORITHM)
        return token
    except JWTError:
       return  JSONResponse(
            status_code=400,
            content={
                "status":"JWT ERROR HERE create refresh"
            }
        )

async def verify_refresh_token(ref_tok:str,db:AsyncSession):
    try:
        decoded_data=jwt.decode(ref_tok,Setting().SECRET_KEY,algorithms=Setting().ALGORITHM)
        email1=decoded_data.get("email")
        result = await db.execute(select(impexp).where(impexp.email==email1))
        data=result.scalars().first()
        if data is None:
            return JSONResponse(
                status_code=400,
                content={
                "refresh token invalid"
                }
            )
        else:
            return {"email":data.email}
    except JWTError:
        return  JSONResponse(
            status_code=400,
            content={
                "status":"refresh token exp"
            }
        )

        
async def create_access_token(ref_tok:str,db:AsyncSession):
    try:
        verification=await verify_refresh_token(ref_tok,db=db)
        encode=verification.copy()
        exp=datetime.utcnow()+timedelta(minutes=5)
        encode.update({"exp":exp})
        acc_token=jwt.encode(encode,Setting().SECRET_KEY,algorithm=Setting().ALGORITHM)
        return acc_token
    except JWTError:
       return  JSONResponse(
            status_code=400,
            content={
                "status":"acc token exp"
            }
        )
    
async def verify_acc_token(acc_tok:str,db:AsyncSession=Depends(get_db)):
    try:
        decoded_data=jwt.decode(acc_tok,Setting().SECRET_KEY,algorithms=Setting().ALGORITHM)
        email=decoded_data.get("email")
        result=await db.execute(select(impexp).where(impexp.email==email))
        data=result.scalars().first()
        if data is None:
            return JSONResponse(
                status_code=400,
                content={
                    "status":"invalid acc token"
                }
            )
        else:
            return data.email
    except JWTError:
        return JSONResponse(
            status_code=400,
            content={
                "status":"acc token expired"
            }
        )
