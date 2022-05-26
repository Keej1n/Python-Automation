# import section
import argparse
import sys
import json
import requests
from marshmallow import Schema, fields, ValidationError
# global variables section
endpoint = "https://jsonplaceholder.typicode.com/posts"
header = {'Content-type': 'application/json'}
# local functions section


class PersonSchema(Schema):
    body = fields.String(required=True)
    title = fields.String(required=True)
    userId = fields.Integer(required=True)
    id = fields.Integer(required=True)
# main block


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=argparse.FileType(),
                        default="task1.json",
                        help="json file to load")
    exit_code = 0
    try:
        args = parser.parse_args()
        data = json.load(args.input)
        response = requests.post(endpoint, json=data, headers=header)
        if response.status_code not in (200, 201, 202):
            raise Exception("Non-successful HTTP request")
        posted_data = json.loads(response.text)
        exit_code = 1
    except Exception as x:
        sys.stderr.write(str(x))
        sys.exit(2)
    try:
        result = PersonSchema().load(posted_data)
    except ValidationError as x:
        print(x.messages)
    else:
        print("OK")
    print(f"request duration = {response.elapsed}")
    sys.exit(exit_code)
