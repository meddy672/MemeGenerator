from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DOCXIngestor(IngestorInterface):
    """Strategy object for docx files."""

    allowed_extensions = ['docx']

    def __init__(self) -> None:
        super().__init__()


    
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse docx files to be ingested
        
        :param (path): path to the docx file that will be ingested
        """
        pass