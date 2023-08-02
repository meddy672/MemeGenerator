from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
class CSVIngestor(IngestorInterface):
    """Strategy object for csv files."""

    allowed_extensions = ['csv']

    def __init__(self) -> None:
        super().__init__()


    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse csv files to be ingested
        
        :param (path): path to the csv file that will be ingested
        """
        pass
