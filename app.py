# coding: utf8
from __future__ import unicode_literals

import hug
from hug_middleware_cors import CORSMiddleware
    

@hug.get('/test')
def parse(model: str, text: str):    
    return 'Hi! Test server!'

if __name__ == "__main__":
    import waitress

    app = hug.API(__name__)
    app.http.add_middleware(CORSMiddleware(app))
    waitress.serve(__hug_wsgi__, port=8080)