import csv
from fastapi import FastAPI, Request, Response, logger

app = FastAPI()

@app.post("/log-error")
async def log_error(request: Request):
    # Parse the JSON-encoded error message from the request
    requestInfo = await request.json()
    logger.info(type(requestInfo))
    logger.info(requestInfo)
    #error_message = requestInfo["error"]

    # Open the CSV file in append mode
    #with open("errors.csv", "a") as csvfile:
        #writer = csv.writer(csvfile)
        # Write the error message to the CSV file
        #writer.writerow([error_message])
    #logger.info("Wrote new error to csv")
    # Return a success response
    return {"status": "SUCCESS"}
