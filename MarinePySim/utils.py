"""
Utils for package
"""
import requests

def get(url, args, ctype, **kwargs):
    """
    return response from api
    """
    out = requests.get(url, params=args, **kwargs)
    return 1