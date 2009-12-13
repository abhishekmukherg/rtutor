===========================
rtutor Tutoring Application
===========================

This project is a simple tutoring ticketing system for RPI.


----------------------------------
Setting up development environment
----------------------------------

There are a few ways you can do this. I personally use buildout and virtualenv:

Either way. you will need django-evolution::

  cd /tmp
  svn co http://django-evolution.googlecode.com/svn/trunk django-evolution
  easy_install /tmp/django-evolution


buildout::

  cd $src_dir
  buildout
  # Run the server
  ./bin/django runserver

Another alternative is to use Distribute::

  cd $src_dir
  python setup.py develop
  DJANGO_SETTINGS_MODULE=rtutor.settings ./bin/rtutor runserver

