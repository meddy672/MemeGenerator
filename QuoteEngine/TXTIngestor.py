from .IngestorInterface import IngestorInterface

class TXTIngestor(IngestorInterface):
    """Strategy object for txt files"""

    allowed_extensions = ['txt']

    def __init__(self) -> None:
        super().__init__()