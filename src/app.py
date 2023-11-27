from .modules.scrapper import FlipkartDataHandler
import aiohttp
from fastapi import FastAPI


class Scrapper:
    """Base Scrapper class
    """
    session = None

    def __init__(self,
                 productName,
                 dbCursor,
                 dbConnection) -> None:
        self.session = aiohttp.ClientSession()
        self.productName = productName
        self.flipkartScrapper = FlipkartDataHandler(
            session=self.session,
            productName=self.productName,
            dbCursor=dbCursor,
            dbConnection=dbConnection
        )

    @classmethod
    def create(cls):
        cls.session = aiohttp.ClientSession()
        return cls.session

    @classmethod
    def close(cls):
        if cls.session is not None:
            return cls.session.close()


async def close():
    await Scrapper.close()
