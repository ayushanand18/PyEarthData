"""
PyEarthData package
~~~~~~~~~~~~~~~~~~~~~

PyEarthData is a python Simulator for dissolved Ocean gases and Marine Species Analysis

Example usage:

# Import entire package
import pyearthdata
# or import modules as needed
## ocean
from pyearthdata import airs

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
from MarinePySim import ocean
___ some sample requests ___
"""

__version__ = "1.0.0"
__title__ = "PyEarthData"
__author__ = "Ayush Anand"
__license__ = "MIT"

__all__ = [
    "airs",
    "power",
]
