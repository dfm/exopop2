# -*- coding: utf-8 -*-

from __future__ import division, print_function

__all__ = ["get_catalog", "get_kois", "get_stlr"]

import os
import requests
import pandas as pd
from cStringIO import StringIO


def get_catalog(name, basepath="data"):
    fn = os.path.join(basepath, "{0}.h5".format(name))
    if os.path.exists(fn):
        return pd.read_hdf(fn, name)
    print("Downloading {0}...".format(name))
    url = ("http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/"
           "nph-nstedAPI?table={0}&select=*").format(name)
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        r.raise_for_status()
    fh = StringIO(r.content)
    df = pd.read_csv(fh)
    df.to_hdf(fn, name, format="t")
    return df


get_kois = lambda: get_catalog("q1_q16_koi")
get_stlr = lambda: get_catalog("q1_q16_stellar")
# get_kois = lambda: get_catalog("q1_q17_dr24_koi")
# get_stlr = lambda: get_catalog("q1_q17_dr24_stellar")
