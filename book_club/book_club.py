"""
Reading Club
Hosted on http://elijahcaine.me/bookclub/

'It ain't supposed to be pretty, it's just supposed to work.'
    - me. right now.
"""

from docutils.core import publish_parts
from jinja2 import Environment, FileSystemLoader
from os.path import isfile
from os import getcwd
import requests



def test_files():
    yell = ''
    needed = ["template.jinja", "book-club.rst", "style.css"]
    for n in needed:
        if not isfile(n):
            yell += n + " does not appear to be available.\n"
    if yell:
        raise Exception(yell + " run `book-club setup` to fix it.")
        exit(1)


def build():
    test_files()
    with open('book-club.rst') as f:
        content = publish_parts(f.read(), writer_name='html')
        title = content['title']
        body =  content['html_body'].replace('\n',' ')

    with open('template.jinja', 'r') as f:
        loader = FileSystemLoader(getcwd())
        env= Environment(loader=loader)
        template = env.get_template('template.jinja')
        page =  template.render(title=title,
                                content=body)

    with open('index.html', 'w') as f:
        f.write(page)


def setup():
    if not isfile("style.css"):
        download('https://raw.githubusercontent.com/ElijahCaine/book_club/master/style.css', 'style.css')
        print("Downloaded example style.css")
    if not isfile("template.jinja"):
        download('https://raw.githubusercontent.com/ElijahCaine/book_club/master/template.jinja', 'template.jinja')
        print("Downloaded example template.jinja")
    if not isfile("book-club.rst"):
        download('https://raw.githubusercontent.com/ElijahCaine/book_club/master/book-club.rst', 'book-club.rst')
        print("Downloaded example book-club.rst")


def download(url=None, file=None):
    print("Downloading " + file + " from " + url)
    r = requests.get(url)
    with open(file, "wb") as f:
        f.write(r.content)
