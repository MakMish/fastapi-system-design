import random
from src.dbmodel import Setting
import ssl
from pydantic import EmailStr
import smtplib
from src.dbmodel import Setting
from celery import Celery

celery_app=Celery("mytask",broker=Setting().redis_url,backend=Setting().redis_url)
celery_app.conf.broker_use_ssl = {
    "ssl_cert_reqs": ssl.CERT_NONE
}

celery_app.conf.redis_backend_use_ssl = {
    "ssl_cert_reqs": ssl.CERT_NONE
}
@celery_app.task(max_retries=3)
def asre(email:EmailStr):
    otp = random.randint(100000,999999)
    message=f"'hey how is it going there hope fine so your otp is {otp} '"
    server=smtplib.SMTP("smtp.gmail.com",587,timeout=10)
    server.starttls()
    server.login("newsrelos@gmail.com",password=Setting().gmail_app_password)
    server.sendmail(from_addr="newsrelos@gmail.com",to_addrs=str(email),msg=message)
    server.quit()
    return{
        "status":"done"
    }

# cmd is celery -A tasks.celery_app worker --pool=solo --loglevel=info 