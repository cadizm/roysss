
Test Local Deployment
=====================

The basic idea for testing local deployment is to create a new virtualbox
instance that mimics the production vps host (e.g. digital ocean).

```
$ vagrant up
$ make deploy_local
```

Secrets
=======

Environment variables and other secrets need to be read manually as needed
from `secrets` file in the project's root directory.


Installing pip Packages
=======================

For installing `cryptography`

```
$ env ARCHFLAGS="-arch x86_64" LDFLAGS="-L/usr/local/opt/openssl/lib" CFLAGS="-I/usr/local/opt/openssl/include" pip install cryptography
```
