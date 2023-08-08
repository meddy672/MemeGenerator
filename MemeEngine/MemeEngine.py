"""Module for the MemeEngine."""
import textwrap
from random import randrange, randint
from PIL import Image, ImageDraw, ImageFont

class MemeEngine:
    """Model for generating memes."""

    def __init__(self, output_dir='./out_img') -> None:
        """Instantiate object."""
        self.output_dir = output_dir

    
    def make_meme(self, img_path, text:str, author:str, width=500) -> str:
        """Core functionality of the application.
        
        Arguments:
        :image_path (str): path to the image of the meme
        :text (str): quote displayed on the meme 
        :author (str): author of the meme.
        :width: (int): width of the meme

        Returns path of the generated meme.
        """
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

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        text_x_position = randint(10, 150)
        text_y_position = height // 2
        counter = 0
        for line in textwrap.wrap(self.text, 25):
            draw.text((text_x_position, (text_y_position + counter)), text=line, font=font, fill='white')
            counter += 20
        draw.text((text_x_position, (text_y_position + counter + 20)), text=f'{self.author}', font=font, fill='white')

        try:
            extension = img_path.split('.')[-1]
            filename = f'{randint(0,1000000)}'
            destination = self.output_dir + '/' + filename + '.' + extension
            img.save(destination, format='JPEG')
        except:
            raise Exception('cannot save image into file')

        return destination
    
