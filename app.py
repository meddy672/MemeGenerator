"""Main Module."""
import random
import os
import requests
from flask import Flask, render_template, request

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))


    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
            imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    extension = image_url.split('.')[-1]
    if image_url is None or image_url == '':
        return render_template('error.html', error='Image url is required')
    elif body is None or body == '':
        return render_template('error.html', error='Quote body is required')
    elif author is None or author == '':
        return render_template('error.html', error='Author is required')

    result = requests.get(image_url)
    
    tmp = f'./tmp/{random.randint(0, 1000000)}.{extension}'
    with open(tmp, 'wb') as img:
        img.write(result.content)

    try:
        path = meme.make_meme(tmp, body, author)
    except:
        raise Exception('could not generate meme')
    
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
