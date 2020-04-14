# -----------------------------------------------------------------------------
# Alpha Forex
# -----------------------------------------------------------------------------
# Author: Maxime Sirois
# -----------------------------------------------------------------------------
"""
Foreign Exchange Personal Assistant
"""
# -----------------------------------------------------------------------------


import argparse
import logging
from pathlib import Path
import sys

from lib.alpha_forex import constants as C
from lib.alpha_forex import utils
from lib.alpha_forex import api


def parse_args(args):
    """
    Argument parser
    :return: Parsed arguments object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Increases verbosity")
    parser.add_argument("--silent", action="store_true", help="Turns off verbose")
    return parser.parse_args(args)


def set_log(log_file_path, debug=False, silent=False):
    """
    Set log configurations.

    Args:
        log_file_path (str): Absolute log file path.
        debug (bool): Set log level to DEBUG (True), otherwise INFO.
        silent (bool): Activates logging on console (False).

    Returns:
        None
    """
    if debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level,
                        format='[%(asctime)s] %(name)-8s - %(levelname)-8s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=log_file_path,
                        filemode='w')

    if not silent:
        console = logging.StreamHandler()
        console.setLevel(level)
        formatter = logging.Formatter('%(levelname)-8s : %(message)s')
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)


def main(argv, verbose=True):
    """
    Main Program Launching
    """
    args = parse_args(argv)
    config = C.get_config(credentials=True)

    # ----- LOGGING SETUP ------------------------
    LOG_LOCATION = Path(config.get('GENERAL', 'LOG_DIR'))
    BATCH_ID = utils.now('%Y%m%d%H%M%S')
    log_file_path = LOG_LOCATION / f'alpha_forex_{BATCH_ID}.log'
    set_log(str(log_file_path), args.debug, args.silent)
    if not verbose:
        logging.getLogger().setLevel(logging.CRITICAL)
    # --------------------------------------------

    # DEFINE GENERAL VARIABLES FROM CONFIG
    API_KEY = config.get('API', 'API_KEY')
    URL = config.get('API', 'URL')

    alphaclient = api.AlphaVantageClient(url=URL, api_key=API_KEY)

    response = alphaclient.get_rate('USD', 'JPY')

    print(response.text)


if __name__ == '__main__':
    main(sys.argv[1:])
