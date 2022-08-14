"""
MarinePySim package
~~~~~~~~~~~~~~~~~~~~~

MarinePySim is a python Simulator for dissolved Ocean gases and Marine Species Analysis

Example usage:

# Import entire package
import MarinePySim
# or import modules as needed
## ocean
from MarinePySim import ocean

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

__version__ = "0.0.1"
__title__ = "MarinePySim"
__author__ = "Ayush Anand"
__license__ = "MIT"

from .ocean import search

__all__ = [
    "ocean",
]
