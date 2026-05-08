from google import genai
from fastapi.requests import Request
from fastapi.responses import JSONResponse
import redis
from src.dbmodel import Setting
client=genai.Client(api_key=Setting().ai_api)
r=redis.from_url(Setting().redis_url)
async def aiit(request: Request, task: str):
    try:

        key = f"{request.client.host}:ai"

        count = r.incr(key)

        if count == 1:
            r.expire(key, 60)

        if count > 3:
            return JSONResponse(
                status_code=429,
                content={
                    "status": "limit_exceeded"
                }
            )

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=f"{task.strip()}, reply in hinglish"
        )

        return JSONResponse(
            status_code=200,
            content={
                "status": response.text
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={
                "status": f"{e}"
            }
        )