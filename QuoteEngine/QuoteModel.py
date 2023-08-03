"""An object for creating Quotes."""

class QuoteModel:
    """Creates quotes."""

    def __init__(self, body:str, author:str) -> None:
        """Instantiate object."""
        self.body = body
        self.author = author