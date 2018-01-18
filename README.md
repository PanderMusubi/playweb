# Playweb

Play audio om remote device via web interface


## Python

Install Python WSGI suport with:

    sudo apt-get install python3-webob

Install Pygame with:

    sudo apt-get install python3-pygame

but to get the latest version, you might want to add the PPA from
https://launchpad.net/~thopiekar/+archive/ubuntu/pygame before you install it.


## jQuery

From http://jquery.com/download/ download the compressed production build:

    wget https://code.jquery.com/jquery-3.2.1.min.js

Remember to add this file to git.


## jQuery Mobile

From http://jquerymobile.com/download/ download the zip file:

    wget http://jquerymobile.com/resources/download/jquery.mobile-1.4.5.zip
    unzip jquery.mobile-1.4.5.zip
    rm -rf jquery.mobile-1.4.5.zip demos

As the non-minimized files are not used, remove those too:

    rm -rf jquery.mobile-1.4.5.css \
    jquery.mobile-1.4.5.js \
    jquery.mobile.external-png-1.4.5.css \
    jquery.mobile.icons-1.4.5.css \
    jquery.mobile.inline-png-1.4.5.css \
    jquery.mobile.inline-svg-1.4.5.css \
    jquery.mobile.structure-1.4.5.css \
    jquery.mobile.theme-1.4.5.css

Remember to add the remaining jQuery files and images directory to git.


## Testing

To test at http://localhost:8000/ start the implementation with:

    ./index.wsgi

Each time the file source files have been edited, the test has to be restarted.


## Upgrading

Remove all old jQuery files:

    git rm -r jquery* images

and download latest version. Make sure to add the new files to git and bumb the
version numbers in the header of the WSGI files. Please, update download
documentation above too.
