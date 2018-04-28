from flask import Blueprint, render_template, request
from ..common.GenerateSnippet import GenerateSnippet

pages_app = Blueprint('pages_app', __name__)

END_OF_LINE_SEQUENCES = {"CR" : "\r", "LF": "\n", "CRLF" : "\r\n"}
SPACES_COUNT = 10

@pages_app.route('/')
def home():
    """Doc string."""
    return render_template('home.html', code='', endOfLineSequences=END_OF_LINE_SEQUENCES, spacesCount=SPACES_COUNT, snippet='')

@pages_app.route('/about')
def about():
    """Doc string."""
    return render_template('about.html')

@pages_app.route('/generateSnippet', methods = ['POST'])
def generate_Snippet():
    """Doc string."""
    key = request.form['keyInput']
    description = request.form['snippetDescriptionInput']
    prefix = request.form['prefixInput']
    tabSize = request.form['tabSizeSelection']
    code = request.form['codeInput']
    selectedlineSequence = request.form['lineEndingSelection']
    endOfLineSequence = END_OF_LINE_SEQUENCES[selectedlineSequence]

    snippet = GenerateSnippet(code, endOfLineSequence, int(tabSize), key, prefix, description)

    return render_template('home.html', code=code, endOfLineSequences=END_OF_LINE_SEQUENCES, spacesCount=SPACES_COUNT, snippet=snippet)

