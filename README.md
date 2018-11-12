# Playweb

Play audio file exists on a remote device via a web interface.


## Python

Install Python WSGI suport with:

    sudo apt-get install python3-webob

Install Pygame with:

    sudo apt-get install python3-pygame

but to get the latest version, you might want to add the PPA from
https://launchpad.net/~thopiekar/+archive/ubuntu/pygame before you install it.


## Testing

To test at http://localhost:8000/ start the implementation with:

    ./index.wsgi

Each time the file source files have been edited, the test has to be restarted.
