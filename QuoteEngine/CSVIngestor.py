"""A strategy object for ingesting csv files.

"""
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
class CSVIngestor(IngestorInterface):
    """Strategy object for csv files."""

    allowed_extensions = ['csv']

    def __init__(self) -> None:
        super().__init__()


    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse csv files to be ingested
        
        :param (path): path to the csv file that will be ingested
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quotes = []

        csv = pandas.read_csv(path, header=0)

        for index, row in csv.iterrows():
            new_quote =  QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
