"""Module for the MemeEngine."""

from random import randrange, randint
from PIL import Image, ImageDraw, ImageFont

class MemeEngine:
    """Model for generating memes."""

    def __init__(self, output_dir='./out_img') -> None:
        """Instantiate object."""
        self.output_dir = output_dir

    
    def make_meme(self, img_path, text:str, author:str, width=500) -> str:
        self.img_path = img_path
        self.text = text
        self.author = author
        self.width = width

        try:
            img = Image.open(self.img_path)
        except(FileNotFoundError):
            raise Exception('cannot open image')
        
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        message = f'{self.text} - {self.author}'
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        text_x_position = randrange(width // 4)
        text_y_position = randrange(width // 2)
        draw.text((text_x_position, text_y_position), message, font=font, fill='white')

        try:
            extension = img_path.split('.')[-1]
            filename = f'{randint(0,1000000)}'
            destination = self.output_dir + '/' + filename + '.' + extension
            img.save(destination, format='JPEG')
        except:
            raise Exception('cannot save image into file')

        return destination
    
