from flask import Flask, request, jsonify, make_response
import spacy

app = Flask(__name__)

def build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
    
def doc2json(doc: spacy.tokens.Doc):
    json_doc = {
        'text': doc.text,
        'text_with_ws': doc.text_with_ws,
        'cats': doc.cats,
        'is_tagged': doc.is_tagged,
        'is_parsed': doc.is_parsed,
        'is_sentenced': doc.is_sentenced
    }
    ents = [{
        'text': ent.text,
        'start': ent.start,
        'end': ent.end,
        'label': ent.label_
    } for ent in doc.ents]
    
    return {        
        'doc': json_doc,
        'ents': ents
    }



@app.route("/")
def index():
    return "Hello World!"

@app.route("/test")
def test():
    return "Test!"

@app.route("/ent",methods=['POST', 'OPTIONS'])
#def ent(text: str):
def ent():
    if request.method == "OPTIONS": # CORS preflight
        return build_cors_preflight_response()
    elif request.method == "POST": # The actual request following the preflight
        content = request.json    
        text = content['text']
        """Get entities for displaCy ENT visualizer."""
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)              
        return corsify_actual_response(jsonify(doc2json(doc)))
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))




