`book-club build`
=================
`book_club` is a little python tool used to automate the upkeep of my book
club.

All you need to do is update the appropriate variables in the book-club.rst
file and run `book-club build`. It'll generate an index.html file and you're
good to go.

Installation:
-------------

.. code::

    $ pip install git+https://github.com/ElijahCaine/book_club.git

Setup
-----
Here's what your directory structure should look like

.. code::

    yourdomain.bla/
        bookclub/
            book-club.rst
            style.css
            template.jinja

`bookclub` is however you want to call `yourdomain.ext/bookclub/`.

For an exmample of book-club.rst, template.jinja, and style.css check out the
ones in this repo.
