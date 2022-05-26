# import section
import argparse
import json
import sys

from marshmallow import Schema, fields
from deepdiff import DeepDiff

# global variables section


# local functions section

class ValidationSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)
    weight = fields.Integer(required=True)

# main block


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog=sys.argv[0])

    parser.add_argument("--file1", type=argparse.FileType(), help="First file to compare")

    parser.add_argument("--file2", type=argparse.FileType(), help="Second file to compare")

    exit_code = 0

    try:
        args = parser.parse_args()
        data1 = json.load(args.file1)
        data2 = json.load(args.file2)
        for data in (data1, data2):
            ValidationSchema().load(data, unknown='EXCLUDE')
        diff = DeepDiff(data1, data2, ignore_order=True)
        if diff:
            with open('output.json', "w") as of:
                json.dump([data1, data2], of)
                of.close()
        exit_code = 1
    except Exception as x:
        sys.stderr.write(str(x) + "\n")
        sys.exit(-1)
    sys.exit(exit_code)
