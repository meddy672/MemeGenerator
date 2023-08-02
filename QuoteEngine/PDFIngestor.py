from .IngestorInterface import IngestorInterface

class PDFIngestor(IngestorInterface):
    """Stratgey object for docx files."""

    allowed_extensions = ['pdf']

    def __init__(self) -> None:
        super().__init__()