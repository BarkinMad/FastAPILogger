from fastapi import FastAPI, logger
from fastapi.responses import FileResponse
from pydantic import BaseModel
import csv

app = FastAPI()

@app.post("/log-error")
async def log_error(error: str):
    with open("errors.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([error])
    logger.info("Logged new error to csv.")
    return FileResponse("errors.csv")