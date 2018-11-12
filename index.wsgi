#!/usr/bin/env python3

from wsgiref.simple_server import make_server
from webob import Request
from cgi import escape
from os import listdir


def playweb_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Playweb</title>
    <link rel="icon" href="favicon.ico" />
</head>
<body style="font-variant-ligatures: none;"><!--TODO ligaturen uitzetten -->
    <!--h1>Playweb</h1-->

'''
    word = ''
    if environ['REQUEST_METHOD'] == 'POST':
        req = Request(environ)
#        word = unicode(req.params.get('name', 'default')).encode('utf-8') ## escape(...)
        word = req.params.get('sound', '').strip() #TODO get value from value from submit
        print(word)

    for fname in sorted(listdir('sounds')):
        if fname.endswith('.wav') or fname.endswith('.ogg'):
            html += '''
<form action="." method="post" class="ui-filterable">
<input data-theme="b" value="{}" type="submit" name="sound"/>
</form>'''.format(fname)

    html += '''
</body>
</html>'''
    return [html.encode('utf-8')]


def application(environ, start_response):
    return playweb_app(environ, start_response)

if __name__ == '__main__':
    httpd = make_server('', 8000, playweb_app)
    print("Serving on port 8000...")
    httpd.serve_forever()
