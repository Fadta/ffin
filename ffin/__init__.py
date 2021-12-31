import logging as log
from os.path import dirname, abspath
from pathlib import Path

ROOT_DIR = dirname(abspath(__file__))
HOME_DIR = Path('~/ffin')

status_log = log.getLogger('status')
execution_log = log.getLogger('exec')
