from fastapi import FastAPI, Request
from .app import Scrapper
import uvicorn
import asyncio
from .helpers import logger
from .app import close

app = FastAPI()


@app.get('/{productName}')
async def productData(productName: str, request: Request):
    scrapperObj = Scrapper(productName=productName)
    jsonData = await scrapperObj.flipkartScrapper.getFlipkartData()
    await scrapperObj.session.close()
    return {
        "client_host": request.client.host,
        "data": jsonData
    }


try:
    uvicorn.run(app)
except Exception as e:
    logger.critical(e)
