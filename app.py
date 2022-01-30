# coding: utf8
from __future__ import unicode_literals

import hug
from hug_middleware_cors import CORSMiddleware
    
@hug.get() # <- Is the hug METHOD decorator
def hello_world():
    return "Hello"

@hug.get('/test')
def test():    
    return 'Hi! Test server!'

print("TEST __name__"+__name__)
if __name__ == "__main__":
    import waitress

    app = hug.API(__name__)
    app.http.add_middleware(CORSMiddleware(app))
    waitress.serve(__hug_wsgi__, port=8080)