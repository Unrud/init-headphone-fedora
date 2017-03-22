# init-headphone-fedora
Manage the headphone amplifier found in some Clevo laptops.
Can initialize the device if headphones are not working after suspend.

**Fedora package for [init-headphone](https://github.com/Unrud/init-headphone)**

## Installation
Go to [releases](https://github.com/Unrud/init-headphone-fedora/releases),
download the package for your distribution and install it.

## Build package
To build the package run:

    spectool -g -R init-headphone.spec
    rpmbuild -bb init-headphone.spec
