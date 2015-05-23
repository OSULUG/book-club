"""
Reading Club
Hosted on http://elijahcaine.me/bookclub/

'It ain't supposed to be pretty, it's just supposed to work.'
    - me. right now.
"""
from yaml import load
from jinja2 import Environment, FileSystemLoader
from os.path import isfile
from os import getcwd
import requests


def test_files():
    yell = ''
    needed = ["template.jinja", "book-club.yml", "style.css"]
    for n in needed:
        if not isfile(n):
            yell += n + " does not appear to be available.\n"
    if yell:
        raise Exception(yell + " run `book-club setup` to fix it.")
        exit(1)

def build():
    test_files()
    with open('book-club.yml') as f:
        cfg = load(f)

    with open('template.jinja', 'r') as f:
        loader = FileSystemLoader(getcwd())
        env= Environment(loader=loader)
        template = env.get_template('template.jinja')
        page =  template.render(release=cfg['release'],
                                title=cfg['title'],
                                site_title=cfg['site_title'],
                                preamble=cfg['preamble'],
                                tagline=cfg['tagline'],
                                this_month_book=cfg['this_month_book'],
                                this_month_link=cfg['this_month_link'],
                                start_date=cfg['start_date'],
                                end_date=cfg['end_date'],
                                meetup_location=cfg['meetup_location'],
                                pacing=cfg['pacing'],
                                encouragement=cfg['encouragement'],
                                disclaimer=cfg['disclaimer'],
                                explanation_title=cfg['explanation_title'],
                                explanation=cfg['explanation']
                                )

    with open('index.html', 'w') as f:
        f.write(page)

def setup():
    if not isfile("style.css"):
        download('https://raw.githubusercontent.com/ElijahCaine/book_club/master/style.css', 'style.css')
        print("Downloaded example style.css")
    if not isfile("template.jinja"):
        download('https://raw.githubusercontent.com/ElijahCaine/book_club/master/template.jinja', 'template.jinja')
        print("Downloaded example template.jinja")
    if not isfile("book-club.yml"):
        download('https://raw.githubusercontent.com/ElijahCaine/book_club/master/book-club.yml', 'book-club.yml')
        print("Downloaded example book-club.yml")

def download(url=None, file=None):
    print("Downloading " + file + " from " + url)
    r = requests.get(url)
    with open(file, "wb") as f:
        f.write(r.content)
