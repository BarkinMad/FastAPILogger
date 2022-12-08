import csv
from fastapi import FastAPI, Request, Response, logger

app = FastAPI()

@app.post("/log-error")
async def log_error(request: Request, response: Response):
    # Parse the JSON-encoded error message from the request
    error_message = await request.json()["error"]

    # Open the CSV file in append mode
    with open("errors.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        # Write the error message to the CSV file
        writer.writerow([error_message])
    logger.info("Wrote new error to csv")
    # Return a success response
    return {"success": True}
