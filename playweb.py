from cgi import escape
from os import listdir
from subprocess import run
from webob import Request
from wsgiref.simple_server import make_server


def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    html = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
<title>Playweb</title>
</head>
<body>
<a href="."><h1>Playweb</h1></a>
<form action="." method="post">
'''
    file = ''
    if environ['REQUEST_METHOD'] == 'POST':
        req = Request(environ)
        file = req.params.get('file', '').strip()
        if file != '':
            run(['aplay', '-q', 'sounds/{}'.format(file)])

    for fname in sorted(listdir('sounds')):
        if fname.endswith('.wav'):
            html += '''<div class="form-group">
<button type="submit" class="btn btn-primary" name="file" value="{}">{}</button>
</div>
'''.format(fname, fname, fname, fname, fname[:-4])

    html += '''</form>
</body>
</html>'''
    return [html.encode('utf-8')]

def application(environ, start_response):
    return app(environ, start_response)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()
