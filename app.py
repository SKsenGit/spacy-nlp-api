from flask import Flask
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
def ent(text: str):
    text = "test my name is Marita"
    """Get entities for displaCy ENT visualizer."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [
        {"start": ent.start_char, "end": ent.end_char, "label": ent.label_}
        for ent in doc.ents
    ]