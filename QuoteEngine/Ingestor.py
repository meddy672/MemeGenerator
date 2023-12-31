"""A final ingestor that selects the approiate helper based in filetype."""

from typing import List
from QuoteEngine.QuoteModel import QuoteModel


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DOCXIngestor import DOCXIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor

class Ingestor(IngestorInterface):
    """Encapsulate Ingestor classes and executes ingestor by file type."""

    ingestors = [TXTIngestor, DOCXIngestor, PDFIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select the appropriate ingestor.

        :param (path): path of the file to ingest.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)