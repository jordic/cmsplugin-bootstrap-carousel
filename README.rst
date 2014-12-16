========================================
Bootstrap carousel plugin for Django-CMS
========================================

.. image:: https://travis-ci.org/nimbis/cmsplugin-bootstrap-carousel.svg?branch=master
   :target: https://travis-ci.org/nimbis/cmsplugin-bootstrap-carousel

.. image:: https://coveralls.io/repos/nimbis/cmsplugin-bootstrap-carousel/badge.png?branch=master
   :target: https://coveralls.io/r/nimbis/cmsplugin-bootstrap-carousel?branch=master

A Django-CMS plugin to easily create carousel components using Bootstrap, from Twitter.
Forked from: https://bitbucket.org/tonioo/cmsplugin-bootstrap-carousel

This plugin supports filer and will use it if it is found in your INSTALLED_APPS.

Requirements
============

* `Django-CMS >= 2.4 <http://django-cms.org>`_
* `Bootstrap <http://twitter.github.com/bootstrap/>`_
* `Pillow`



Installation
============

To use it into your project, just follow this procedure:

#. Install the the plugin in your virtualenv, using::

    pip install 

and remember to add it to your requirements.txt file, if you use one.

#. Open the *settings.py* file and add ``cmsplugin_bootstrap_carousel`` to the
   ``INSTALLED_APPS`` variable

#. Run the following command::

    $ ./manage.py migrate cmsplugin_bootstrap_carousel


.. note::

    Bootstrap is not included with this plugin.

History
=======

Fork:
  * Deleted some options, and adapted to our regular workflow.


0.2.1:

    * Changed plugin name from CarouselPlugin to BootstrapCarouselPlugin to avoid name collision
    with djangocms-cascade.

0.2.0:

    * Added fields for toggling visibility of carousel controls and slide indicator. Improved the included template.