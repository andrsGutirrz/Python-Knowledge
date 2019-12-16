import json
import ast
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
            'reviewer_name': 'JoJo',
            'reviewer_id': 5555,
            'internal_only': 'aaaa',
            'summary': 'bbbb',
        }

        return json.dumps(comment)
    raise Exception("Just GET method supported")


@app.route('/insertComment', methods=['POST'])
def insert_comment():
    if request.method == 'POST':
        variables = []
        # verify if data comes from a form
        if request.form:
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

        else:
            # if data comes from json
            data = request.data.decode("utf-8").replace("\'", "\"")
            obj = ast.literal_eval(data)

        print(variables)

        return json.dumps("Comment inserted")

    raise Exception("Just POST method supported")


app.run(debug=True)
