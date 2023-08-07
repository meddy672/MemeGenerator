# MemeGenerator Project
The goal of this project is to build a multimedia application which dynamically generates memes with an image, author and overlaid quote.

## Table of Content
* Required Software
* Installation
* Usage

### Required Software
* [Python v3.10.6](https://www.python.org/downloads/)
* [Xpdf tool](https://www.xpdfreader.com/download.html)

### Installation
To set up and install the MemeGenerator project on your local machine, follow these steps:
1. Clone Repository
```
git clone https://github.com/meddy672/MemeGenerator.git
```
2. Navigate to the project directoy
```javascript
cd MemeGenerator
```
3. Install the required dependencies
```
pip install -r requirements.txt
```
4. Install Xpdf tool - necessary for the PDFIngestor module
```
sudo apt-get install -y xpdf
```
5. Start Flask server
```
flask run --host 127.0.0.1 --port 3000
```
Access the web application at [http://127.0.0.1:3000](http://127.0.0.1:3000)


## Usage

#### Web Application
Randon dog memes are generated using the application assets. To create a meme, click the creator button, fill-out the create meme form and click **Create Meme!** button.

#### Command Line Interface (CLI)
The command line tool can be used with or without arguments. Basic usage:
```
python meme.py
```






