"""
Utils for MarinePySim package
"""
import requests
__airs_base_url__ = "https://map1.vis.earthdata.nasa.gov/wmts-geo/wmts.cgi"

def get(url, args, ctype, **kwargs):
    """
    return response from api
    """
    out = requests.get(url, params=args, stream=True, **kwargs)
    out.raise_for_status()
    return out