Description
===========
Library that allow application launch lock based on pid.

Development Environment
-----------------------

::

    nibbler:~/dev/pidlock:master$ sudo apt-get install  python-virtualenv
    nibbler:~/dev/pidlock:master$ virtualenv --no-site-packages virtual
    nibbler:~/dev/pidlock:master$ . ./virtual/bin/activate
    (virtual)nibbler:~/dev/pidlock:master$ easy_install zc.buildout
    (virtual)nibbler:~/dev/pidlock:master$ buildout init
    (virtual)nibbler:~/dev/pidlock:master$ python bootstrap.py 
    (virtual)nibbler:~/dev/pidlock:master$ bin/buildout 


Run Tests
---------
::

    (virtual)nibbler:~/dev/pidlock:master$ bin/nosetests pidlock/test.py 
