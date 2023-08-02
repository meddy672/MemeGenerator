from .IngestorInterface import IngestorInterface

class PDFIngestor(IngestorInterface):
    """Stratgey object for docx files."""

    def __init__(self) -> None:
        super().__init__()