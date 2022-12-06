"""
PyEarthData package
~~~~~~~~~~~~~~~~~~~~~

PyEarthData is a python Simulator for dissolved Ocean gases and Marine Species Analysis

Example usage:

# Import entire package
import pyearthdata
# or import modules as needed
## airs
from pyearthdata import airs
## power
from pyearthdata import power

## use advanced logging
### setup first
import requests
import logging
import httplib as http_client
http_client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
### then make request
from MarinePySim import airs
airs.co()
"""

try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"

__title__ = "PyEarthData"
__author__ = "Ayush Anand"
__license__ = "MIT"

__all__ = [
    "airs",
    "power",
]
