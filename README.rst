Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython-circuitpython-parse/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/parse/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/jimbobbennett/CircuitPython_Parse/workflows/Build%20CI/badge.svg
    :target: https://github.com/jimbobbennett/Circuitpython_CircuitPython_Parse/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Parse (absolute and relative) URLs.

This code is taken from the `CPython Parse library <https://github.com/python/cpython/blob/master/Lib/urllib/parse.py>`_, and tweaked to work under CircuitPython.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-parse/>`_. To install for current user:

.. code-block:: shell

    pip3 install circuitpython-parse

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-parse

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install circuitpython-parse

Usage Example
=============

Parse a URL.

.. code-block:: python

    url = "https://docs.microsoft.com/Learn?WT.mc_id=academic-0000-jabenn"

    scheme, netloc, path, params, query, fragment = parse.urlparse(url)

    print("Scheme", scheme)
    print("Netloc", netloc)
    print("Path", path)
    print("Params", params)
    print("Query", query)
    print("Fragment", fragment)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/jimbobbennett/CircuitPython_Parse/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
