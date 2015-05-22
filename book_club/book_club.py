"""
Reading Club
Hosted on http://elijahcaine.me/bookclub/

'It ain't supposed to be pretty, it's just supposed to work.'
    - me. right now.
"""
from yaml import load
from jinja2 import Environment, PackageLoader

def build():
    with open('book-club.yml') as f:
        cfg = load(f)

    with open('template.jinja', 'r') as f:
        env = Environment(loader=PackageLoader('book-club', '.'))
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
