from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/test")
def test():
    return "Test!"

@app.route("/ent",methods=['POST'])
#def ent(text: str):
def ent():
    content = request.json    
    text = content['text']
    """Get entities for displaCy ENT visualizer."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    response = jsonify(doc2json(doc))
    response.headers.add('Access-Control-Allow-Origin', '*')
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
        'start': ent.start,
        'end': ent.end,
        'label': ent.label_
    } for ent in doc.ents]
    sents = [{
        'start': sent.start,
        'end': sent.end
    } for sent in doc.sents]
    noun_chunks = [{
        'start': chunk.start,
        'end': chunk.end
    } for chunk in doc.noun_chunks]
    tokens = [{
        'text': token.text,
        'text_with_ws': token.text_with_ws,
        'whitespace': token.whitespace_,
        'orth': token.orth,
        'i': token.i,
        'ent_type': token.ent_type_,
        'ent_iob': token.ent_iob_,
        'lemma': token.lemma_,
        'norm': token.norm_,
        'lower': token.lower_,
        'shape': token.shape_,
        'prefix': token.prefix_,
        'suffix': token.suffix_,
        'pos': token.pos_,
        'tag': token.tag_,
        'dep': token.dep_,
        'is_alpha': token.is_alpha,
        'is_ascii': token.is_ascii,
        'is_digit': token.is_digit,
        'is_lower': token.is_lower,
        'is_upper': token.is_upper,
        'is_title': token.is_title,
        'is_punct': token.is_punct,
        'is_left_punct': token.is_left_punct,
        'is_right_punct': token.is_right_punct,
        'is_space': token.is_space,
        'is_bracket': token.is_bracket,
        'is_currency': token.is_currency,
        'like_url': token.like_url,
        'like_num': token.like_num,
        'like_email': token.like_email,
        'is_oov': token.is_oov,
        'is_stop': token.is_stop,
        'is_sent_start': token.is_sent_start,
        'head': token.head.i
    } for token in doc]
    return {        
        'doc': json_doc,
        'ents': ents,
        'sents': sents,
        'noun_chunks': noun_chunks,
        'tokens': tokens
    }
    