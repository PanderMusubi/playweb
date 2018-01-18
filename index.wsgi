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
    <link rel="stylesheet" href="jquery.mobile-1.4.5.min.css">
    <link rel="icon" href="favicon.ico" />
    <script src="jquery-3.2.1.min.js"></script>
    <script src="jquery.mobile-1.4.5.min.js"></script>
</head>
<body style="font-variant-ligatures: none;"><!--TODO ligaturen uitzetten -->
<div data-role="page">
<div data-role="header" class="jqm-header">
    <!--h1>Playweb</h1-->
</div><!-- /header -->

<div role="main" class="ui-content jqm-content">
<div id="word" class="ui-body-d ui-content">
'''
    word = ''
    if environ['REQUEST_METHOD'] == 'POST':
        req = Request(environ)
#        word = unicode(req.params.get('name', 'default')).encode('utf-8') ## escape(...)
        word = req.params.get('word', '').strip() #TODO get value from value from submit

    for fname in sorted(listdir('sounds')):
        if fname.endswith('.mp3'):
            html += '''
<form action="." method="post" class="ui-filterable">
<input data-theme="b" value="{}" type="submit" />
</form>'''.format(fname[:-4])

    html += '''
</div><!-- /word -->
</div><!-- /main -->
</div><!-- /page -->
</body>
</html>'''
    return [html.encode('utf-8')]


def application(environ, start_response):
    return playweb_app(environ, start_response)

if __name__ == '__main__':
    httpd = make_server('', 8000, playweb_app)
    print("Serving on port 8000...")
    httpd.serve_forever()
