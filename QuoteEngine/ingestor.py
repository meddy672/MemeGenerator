from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if a class can ingest a file based on its file type.
        
        Args:
            path (str): The path to the file.

        Returns:
            bool: True if the class can ingest the file, else returns false.
        """
        pass


    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the DOCX file and return a list of QuoteModel instances.
        
        Args:
            path (str): The path to the DOCX file.

        Retruns:
            List[QuoteModel]: A list of QuoteModel instance representing the quotes found in the DOCX file.
        """
        pass