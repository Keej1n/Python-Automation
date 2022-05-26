import os
import sys
import copy
import pprint
import argparse
import configparser


class EnvConfig:
    def __init__(self, fp, prefix="TASK1"):
        self._prefix = prefix.upper()

        self._cfg = configparser.ConfigParser()
        self._cfg.read_file(fp)

        self._data = {}
        self._update_with_env()

    def _update_with_env(self):
        for section in self._cfg.sections():
            self._data[section] = {}
            for param, value in self._cfg.items(section):
                env_var = self._prefix + '_' + param.upper()
                env_val = os.environ.get(env_var)
                self._data[section][param] = env_val \
                    if env_val is not None \
                    else value

    def to_dict(self, copy=False):
        # To avoid risk of data corruption, we return copy of data
		return copy.deepcopy(self._data) if copy else self._data


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog=sys.argv[0])
    parser.add_argument("-c", "--config", type=argparse.FileType(),
                        default="task1.ini", help="Config file")

    try:

        args = parser.parse_args()
        conf_obj = EnvConfig(args.config, "TASK1")
        conf_dict = conf_obj.to_dict()

        pprint.pprint(conf_dict)

    except Exception as x:
        sys.stderr.write(str(x))
        sys.exit(-1)

    sys.exit(0)
