from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """Stratgey object for docx files."""

    allowed_extensions = ['pdf']

    def __init__(self) -> None:
        super().__init__()


    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse pdf files to be ingested
        
        :param (path): path to the pdf file that will be ingested
        """
        