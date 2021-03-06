# emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 noet:
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the datalad package for the
#   copyright and license terms.
#
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""Install a dataset from a given url

"""

"""
some more bits...

more TODO

Examples:

$ datalad install http://psydata.ovgu.de/forrest_gump/.git /foo/bar

TODO: See TODO.org

"""

__docformat__ = 'restructuredtext'

# magic line for manpage summary
# man: -*- % get a dataset from a remote repository


import calendar
import os
import re
import shutil
import time

import argparse
import os
import sys

import datalad.log
from .helpers import parser_add_common_args

def setup_parser(parser):

    parser.add_argument(
        "source", metavar='url',
        help="url to git repository")

    parser.add_argument(
        "destination", metavar='dir',
        help="path where to store the retrieved dataset")

    #parser_add_common_args(parser, opt=('log_level'))
    
def run(args):
    from datalad.api import Dataset
    from datalad.log import lgr

    lgr.debug("Command line arguments: %r" % args)

    path = os.path.expandvars(os.path.expanduser(args.destination))
    ds = Dataset(path, args.source)


