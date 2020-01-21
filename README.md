# Flight_tracking_master

*Flight Tracking* is a web platform where pilots can share their flights with others
after, or even during flight via live tracking.  *Flight Tracking* is a sort of social
network for pilots including rankings, statistics and other interesting
features.  Most of all *Flight Tracking* is truly open in all regards compared to
other similar platforms.

*Flight Tracking* has started development in 2012 as a spin-off from the popular
[XCSoar](http://www.xcsoar.org/) glide computer. Internally *Flight Tracking* is still
sharing some code with XCSoar in the algorithmic areas and is providing the
base for XCSoar's live tracking functionalities.

*Flight Tracking* is far from finished yet, but it has been running in production for
quite some time now.

## Getting the source

The *Flight Tracking* source code is managed with [git](http://www.git-scm.com/).
It can be downloaded with the following command:

    $ git clone https://github.com/softdev9/flight_tracking_master.git

For more information, please refer to the [git documentation](http://git-scm.com/documentation).

## Installation and Setup

*Flight Tracking* is based on Python and depends on the following major components:

* [PostgreSQL](http://www.postgresql.org/) database with
  [PostGIS 2.x](http://www.postgis.net/) extension
* [Flask](http://flask.pocoo.org/) web application microframework for Python
* [SQLAlchemy](http://www.sqlalchemy.org/) ORM framework with
  [GeoAlchemy 2](https://geoalchemy-2.readthedocs.org) extension
* [gevent](http://www.gevent.org/) coroutine-based network library for Python (used for
  the live tracking server)

The process of installing these components and setting up a server for local
development is described in the [INSTALL.md](INSTALL.md) file.

## Contact and Contributing

Bugs and feature request can be submitted here on
[GitHub](https://github.com/softdev9/flight_tracking_master/issues). New ideas can
also be discussed in the
[Wiki](https://github.com/softdev9/flight_tracking_master/wiki) first.

Patches should be submitted using the
[Pull Request](https://github.com/softdev9/flight_tracking_master/pulls) system of
GitHub because of the integration with

Here are a few guidelines for creating patches:

- patches should be self-contained
- patches should be self-documenting  
  (add a good description on what is changed, and why you are changing it)
- write one patch for one change

