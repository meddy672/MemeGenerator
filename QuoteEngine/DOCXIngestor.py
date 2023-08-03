"""

"""
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DOCXIngestor(IngestorInterface):
    """Strategy object for docx files."""

    allowed_extensions = ['docx']

    def __init__(self) -> None:
        super().__init__()


    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse docx files to be ingested
        
        :param (path): path to the docx file that will be ingested
        """
        if not cls.can_ingest(path):
            raise Exception('coannot ingest exception')
        
        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = parse.textr.split('-')
                new_quote = QuoteModel(parse[0].strip(' "')), parse[1]
                quotes.append(new_quote)

        return quotes