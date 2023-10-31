from ...constants import Common
from .extractor import Extractor


class FlipkartDataHandler:
    def __init__(self, session=None, productName=None) -> None:
        self.session = session
        self.productName = productName

    def getUrl(self):
        return Common.FLIPKART_URL + self.productName

    async def _fetchHtml(self):
        _res = await self.session.post(self.getUrl())

        if _res.status == 200:
            return await _res.text()

        raise InterruptedError(
            f'got error while fetching. status_code: {_res.status}')
        # with open('index.html') as f:
        #     return f.read()

    async def getFlipkartData(self):
        _html = await self._fetchHtml()
        return Extractor(html=_html).extractedRawDataOfDivs()
