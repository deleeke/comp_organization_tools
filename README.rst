Computer Organization Tools
==============================================

.. image:: https://travis-ci.org/deleeke/comp_organization_tools.svg?branch=master
    :target: https://travis-ci.org/deleeke/comp_organization_tools

This module provides some simple utilities for computer organization students.
At the moment, it consists of conversion utilties to and from decimal integers, twos complement binary and hex integers.

----

How to install:
==============================================
This package is compatible with python 2, 2.7, 3, 3.4, 3.5 and possibly others. 
For a system-wide install on linux (and presumably OSX, though I have not tested this) there are 
two options. If you use pip_, you can navigate to the top directory of this project and run::
    # for python 3
    sudo pip3 install comp_organization_tools
    # for python 2
    sudo pip2 install comp_organization_tools
    # Alternatively, you could install with setup.py directly
    # use which ever python you want to install the package to
    sudo python setup.py install

----


Ideas for Contributing:
    * write tests to ensure proper function of all combinations of input/function combinations
    * installation directions for Anaconda users on non-unix based operating systems
    * convert logical expressions to truth tables

.. _pip: https://pypi.python.org/pypi/pip/

Note: this package is based off a sample package from PyPUG's "Tutorial on Packaging and Distributing Projects". Other than the structure of the package, this project shares nothing in commmon with its parent fork.
