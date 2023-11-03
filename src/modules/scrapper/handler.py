from ...constants import Common
from .extractor import Extractor
from ...helpers import logger


class FlipkartDataHandler:
    """flipkart data handler
    """
    def __init__(self, session=None, productName=None) -> None:
        self.session = session
        self.productName = productName

    def getUrl(self):
        # returns the url of the product
        return Common.FLIPKART_URL + self.productName

    async def _fetchHtml(self):

        # asyncronously fetches the response
        async with self.session.post(self.getUrl()) as _res:

            # if status is 200 return the text/html
            if _res.status == 200:
                return (_res, await _res.text())
        # returns None if ran into an error
        return None

    async def getFlipkartData(self):
        # fetches the html and check for status code
        try:
            _res, _html = await self._fetchHtml()
            if _res.status != 200:
                logger.warn(
                    f'failed to fetch html. Status code: {_res.status}')

            # get the Extracted data
            return Extractor(html=_html).extractedDataOfDivs()
        # else return empty dict
        except Exception as e:
            logger.critical(msg=f'failed to get html. needed a restart.{e}')
            return {}
