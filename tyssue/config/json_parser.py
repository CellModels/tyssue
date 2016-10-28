"""Configuration management - json interface
"""

import json
import logging
import os
import warnings

logger = logging.getLogger(__name__)


def load_spec(fname):
    with open(fname, 'r+') as config_file:
        spec = json.load(config_file)
    return spec


def save_spec(spec, fname,
              overwrite=False):
    """Saves a specification file to json

    Parameters
    ----------

    spec : dict,
      The specification nested dictionaries to be saved
    fname: str,
      The file name, can be a path
    overwrite: bool,
      Wheter or not to overwrite an existing file, default False

    """
    if not overwrite:
        if os.path.isfile(fname):
            raise IOError('''%s exists and overwriting is prevented
Please set `overwrite` to True
''' % fname)
    with open(fname, 'w+') as config_file:
        json.dump(spec, config_file)


def load_default(aspect='core', sub_aspect=''):

    warnings.warn('load_default is Deprecated,'
                  ' use methods from config instead')
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    # root = os.path.dirname(cur_dir)

    specfile = os.path.join(cur_dir, aspect, sub_aspect+'.json',)
    logger.info('Loading defaults from {}'.format(specfile))
    if not os.path.isfile(specfile):
        raise IOError('configuration file {} is missing'.format(specfile))

    return load_spec(specfile)
