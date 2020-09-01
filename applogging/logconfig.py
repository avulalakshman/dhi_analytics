import logging
import logging.config
import yaml

with open('resources/logging.yml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
