"""Module for the MemeEngine."""
from PIL import Image, ImageDraw, ImageFont

class MemeEngine:
    """Model for generating memes."""

    def __init__(self, output_dir='./out_img') -> None:
        """Instantiate object."""
        self.out_dir = output_dir 
    
    
