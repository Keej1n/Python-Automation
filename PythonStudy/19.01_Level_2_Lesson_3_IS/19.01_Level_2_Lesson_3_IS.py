# import section
import xmltodict
from marshmallow import fields, Schema
from marshmallow.validate import Range
import json
import logging
import argparse
import sys
# global variables section

# local functions section


class PersonSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(validate=Range(min=18, max=110))


def x2d_postprocess(path, key, value):
    if key == "age":
        value = int(value)
    return key, value
# main block


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=argparse.FileType(), help="Input XML file", required=True)
    parser.add_argument("--output", type=argparse.FileType(mode="w"), help="Output JSON file")
    parser.add_argument("--loglevel", type=str, help="Log level", default="DEBUG")
    parser.add_argument("--logfile", type=str, help="Log file")
    has_logging = False
    try:
        args = parser.parse_args()
        logging.basicConfig(filename=args.logfile,
                            format='%(asctime)s: %(levelname)s:%(message)s',
                            level=logging.getLevelName(f'{args.loglevel}'))
        has_logging = True
        with args.input as file:
            logging.info('XML file has been opened')
            my_dict = xmltodict.parse(file.read(), postprocessor = x2d_postprocess)
        logging.info('XML file is parsed to dictionary')
        dict_data = [dict(x) for x in my_dict["content"]["person"]]
        logging.info("Validating XML content")
        PersonSchema().load(dict_data, many=True)
        logging.info(f"Writing output to {args.output.name}")
        json.dump(dict_data, args.output, indent=4)
        logging.info("Data was saved in output file")
    except Exception as x:
        if has_logging:
            logging.error(str(x))
        else:
            sys.stderr.write(str(x))
        sys.exit(-1)
