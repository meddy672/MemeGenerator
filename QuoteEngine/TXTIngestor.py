from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    """Strategy object for txt files"""

    allowed_extensions = ['txt']

    def __init__(self) -> None:
        super().__init__()


    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse txt files to be ingested
        
        :param (path): path to the txt file that will be ingested
        """
        pass