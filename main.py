from fastapi import FastAPI, Query
from datetime import datetime
import aiofiles
from tasks import send_email_task
import os

app = FastAPI()

@app.get("/")
async def root(sendmail: str = Query(None), talktome: bool = Query(False)):
    if sendmail:
        send_email_task.delay(sendmail)
        return {"message": f"Email will be sent to {sendmail}"}

    if talktome:
        log_message = f"{datetime.now()}\n"
        async with aiofiles.open("/var/log/messaging_system.log", mode="a") as log_file:
            await log_file.write(log_message)
        return {"message": "Current time logged"}

    return {"message": "Invalid request"}
