from .IngestorInterface import IngestorInterface

class DOCXIngestor(IngestorInterface):
    """Strategy object for docx files."""

    def __init__(self) -> None:
        super().__init__()