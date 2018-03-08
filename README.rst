==========
led-tester
==========


.. image:: https://img.shields.io/pypi/v/led_tester.svg
        :target: https://pypi.python.org/pypi/led_tester

.. image:: https://img.shields.io/travis/dillonfr/led_tester.svg
        :target: https://travis-ci.org/dillonfr/led_tester

.. image:: https://readthedocs.org/projects/led-tester/badge/?version=latest
        :target: https://led-tester.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




LED Tester Assignment 3 COMP30670


* Free software: GNU General Public License v3
* Documentation: https://led-tester.readthedocs.io.


Features
--------
Takes in instructions for an LED grid display, counting how many lights are left on after a series of instructions.
Sample instructions:
turn on 10,10 through 90,90
turn off 25,25 through 50,50
switch 0,0 through 99,99


Commands to use this ledtester for local files or http files:

$ solveled --input localfile.txt
$ solveled --input http://a.b.com.txt

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
