"""Strategy object for ingesting pdf files.
"""
import os
import random
import subprocess

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
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', '-raw', path, tmp])
    
        file_ref = open(tmp, "r")
        quotes = []
    
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                new_quote = QuoteModel(parse[0].strip(' "'), parse[1].strip())
                quotes.append(new_quote)
    
        file_ref.close()
        os.remove(tmp)
        return quotes
        