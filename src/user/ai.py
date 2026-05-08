from google import genai
from fastapi.requests import Request
from fastapi.responses import JSONResponse
import redis
from src.dbmodel import Setting
client=genai.Client(api_key=Setting().ai_api)
r=redis.from_url(Setting().redis_url)
async def aiit(request:Request,task:str):
    try:
        if r.get(f"{request.client.host}:ai") > 3:
                return JSONResponse(
            status_code=440,
            content={
                "status":"limit_exceeded"
            }
            )
        v=r.incr(f"{request.client.host}:ai")
        if v==1:
             r.expire(f"{request.client.host}:ai")
        print(v)
        response =client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"'task is {task.strip()}, do it straight to point no any extra gestures and reply in hinglish'"
        )
        return JSONResponse(
            status_code=200,
            content= {
        "status":response.text
        }
        )
    except Exception as  e:
        return JSONResponse(
            status_code=400,
            content={
                "status":f"{e}"
            }
        )