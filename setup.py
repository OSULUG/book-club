from distutils.core import setup

with open('requirements.txt') as f:
    requirements = [l.strip() for l in f]

setup(
    name='book-club',
    version='0.1',
    packages=['book_club'],
    author='Elijah Caine',
    author_email='elijahcainemv@gmail.com',
    url='https://elijahcaine.me/bookclub/',
    description='small prog for management of the for #osu-lug reading club',
    install_requires=requirements,
    scripts=['book_club/book-club']
)
