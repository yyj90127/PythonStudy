import os
import requests
import unittest2

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))

import sys
if PKG_DIR not in sys.path:
    sys.path.append(PKG_DIR)

from tools.csvmanager import readcsv


class ind_Base(unittest2.TestCase):
    @classmethod
    def setUpClass(cls):
        listURL = []
        table = readcsv('url')
        for i in table:
            listURL.append(i)
        cls.BaseURL = f'{listURL[0][0]}'
        cls.request = requests.session()