from ...constants import Common
from .extractor import Extractor
from ...helpers import logger


class FlipkartDataHandler:
    def __init__(self, session=None, productName=None) -> None:
        self.session = session
        self.productName = productName

    def getUrl(self):
        return Common.FLIPKART_URL + self.productName

    async def _fetchHtml(self):
        async with self.session.post(self.getUrl()) as _res:

            if _res.status == 200:
                return (_res, await _res.text())
        return None

    async def getFlipkartData(self):
        try:
            _res, _html = await self._fetchHtml()
            if _res.status != 200:
                logger.warn(
                    f'failed to fetch html. Status code: {_res.status}')
            return Extractor(html=_html).extractedRawDataOfDivs()
        except Exception as e:
            logger.critical(msg=f'failed to get html. needed a restart.{e}')
            return {}
