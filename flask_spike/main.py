import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def main():
    return "Hello World"


@app.route('/getComment', methods=['GET'])
def get_comment():

    if request.method == 'GET':
        comment = {
            'author_name': "Andres Gutierrez",
            'author_id': 6767,
            'reviewer_name': 'Fuli E',
            'reviewer_id': 5555,
            'internal_only': 'internal only section',
            'summary': 'summary section',
        }

        return json.dumps(comment)
    raise Exception("Just GET method supported")


@app.route('/insertComment', methods=['POST'])
def insert_comment():
    if request.method == 'POST':
        variables = []
        author_name = request.form.get('author_name', '')
        author_id = request.form.get('author_id', '')
        reviewer_name = request.form.get('reviewer_name', '')
        reviewer_id = request.form.get('reviewer_id', '')
        internal_only = request.form.get('internal_only', '')
        summary = request.form.get('summary', '')
        variables.append(author_name)
        variables.append(author_id)
        variables.append(reviewer_name)
        variables.append(reviewer_id)
        variables.append(internal_only)
        variables.append(summary)
        print(variables)
        return json.dumps("Comment inserted")

    raise Exception("Just POST method supported")


app.run(debug=True)
