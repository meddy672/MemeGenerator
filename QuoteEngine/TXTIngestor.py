"""Strategy object for ingesting txt files.
"""
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
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        txt = open(path, 'r')

        for line in txt:
            if line != "":
                parse = line.split('-')
                new_quote = QuoteModel(parse[0].strip(), parse[1].strip())
                quotes.append(new_quote)
        txt.close()

        return quotes