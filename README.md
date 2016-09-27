
Test Local Deployment
=====================

The basic idea for testing local deployment is to create a new virtualbox
instance that mimics the production vps host (e.g. digital ocean).

Do a `vagrant up` and set up a local user that has `sudo`.

All other interaction should be done via ansible.


Environment Variables
=====================

These need to be set manually on a per-user basis.

* `DJANGO_SECRET_KEY` (root)
