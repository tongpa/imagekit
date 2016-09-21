# -*- coding: utf-8 -*-
"""
Wkhtmltopdf python wrapper to convert html to Image using the webkit rendering engine and qt
"""

__author__ = 'Tong'
__version__ = '0.1.0'
__license__ = 'MIT'

from .imagekit import ImageKit
from .api import from_url, from_file, from_string, configuration
