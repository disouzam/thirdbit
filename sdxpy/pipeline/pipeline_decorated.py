import sys
import yaml

# [import]
from decorated import EXPORTS as functions
# [/import]

# [func]
def pipeline(config_file, functions):
    with open(config_file, "r") as reader:
        config = yaml.safe_load(reader)

    data = None
    for stage in config:
        func_name, params = stage["name"], stage["params"]
        func = functions[func_name]
        if data is None:
            data = func(*params)
        else:
            data = func(data, *params)

    return data
# [/func]

# [call]
result = pipeline(sys.argv[1], functions)
# [/call]

import csv
csv.writer(sys.stdout).writerows(result)
