import os
import yaml
import copy
from datetime import datetime


CONFIG = None
CONFIG_TTL = 5
CONFIG_TIMESTAMP = 0

def config(key = None):
    global CONFIG, CONFIG_TIMESTAMP
    now_ts = datetime.utcnow().timestamp()
    if CONFIG is None or now_ts - CONFIG_TIMESTAMP >= CONFIG_TTL:
        config_file_name = os.environ.get('CODEGENERATION_CONFIG_FILE')
        assert config_file_name is not None, 'CODEGENERATION config file is not defined, use env variable CODEGENERATION_CONFIG_FILE'
        assert os.path.isfile(config_file_name), f'CODEGENERATION config file ("{config_file_name}") not found'
        with open(config_file_name, encoding='utf8') as config_file:
            CONFIG = yaml.safe_load(config_file.read())
        CONFIG_TIMESTAMP = now_ts
    return copy.deepcopy(CONFIG) if key is None else copy.deepcopy(CONFIG.get(key))
