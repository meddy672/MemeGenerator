from .IngestorInterface import IngestorInterface

class CSVIngestor(IngestorInterface):
    """Strategy object for csv files."""

    allowed_extensions = ['csv']

    def __init__(self) -> None:
        pass