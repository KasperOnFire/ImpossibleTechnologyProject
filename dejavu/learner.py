#!/usr/bin/python
import sys
import json
import warnings
from dejavu import Dejavu


warnings.filterwarnings("ignore")

DEFAULT_CONFIG_FILE = "dejavu.cnf.SAMPLE"

def init(configpath):
    """ 
    Load config from a JSON file
    """
    try:
        with open(configpath) as f:
            config = json.load(f)
    except IOError as err:
        print("Cannot open configuration: %s. Exiting" % (str(err)))
        sys.exit(1)

    # create a Dejavu instance
    return Dejavu(config)


if __name__ == '__main__':

    config_file = DEFAULT_CONFIG_FILE
    djv = init(config_file)
    print("Fingerprinting all files in the learner directory")
    djv.fingerprint_directory("./learn/", ["." + "*"], 4)
    sys.exit(0)