# import section
import argparse
import configparser
import sys
import os
# global variables section
conf = {}
# local functions section


# main block


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(prog=sys.argv[0])
    # parser.add_argument("-c", "--config", type=argparse.FileType(mode="r"), default="task1.ini", required=True)
    cfg = configparser.ConfigParser()
    try:
        # args = parser.parse_args()
        cfg.read("task1.ini")
        for section in cfg.sections():
            conf[section] = {}
            for key, value in cfg.items(section):
                env_var = "TASK1" + '_' + key.upper()
                env_val = os.environ.get(env_var)
                conf[section][key] = env_val \
                    if env_val is not None \
                    else value
        print(conf)
    except (argparse.ArgumentError, argparse.ArgumentTypeError) as x:
        sys.stderr.write(str(x))
        sys.exit(-1)
