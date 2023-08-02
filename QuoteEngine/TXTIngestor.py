from .IngestorInterface import IngestorInterface

class TXTIngestor(IngestorInterface):
    """Strategy object for txt files"""

    def __init__(self) -> None:
        super().__init__()