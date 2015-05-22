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

def test_files():
    yell = ''
    needed = ["template.jinja", "book-club.yml", "style.css"]
    for n in needed:
        if not isfile(n):
            yell += n + " does not appear to be available.\n"
    if yell:
        raise Exception(yell + "Use book_club.setup() to fix it.")

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
                                tagline=cfg['tagline'],
                                this_month_book=cfg['this_month_book'],
                                this_month_link=cfg['this_month_link'],
                                start_date=cfg['start_date'],
                                end_date=cfg['end_date'],
                                meetup_location=cfg['meetup_location'],
                                pacing=cfg['pacing'],
                                encouragement=cfg['encouragement'],
                                )

    with open('index.html', 'w') as f:
        f.write(page)

def setup():
    if not isfile("style.css"):
        print("FIXME add sample style.css where it should go")
    if not isfile("template.jinja"):
        print("FIXME add sample template.jinja where it should go")
    if not isfime("book-club.yml"):
        print("FIXME add sample book-club.yml where it should go")
