"""
AIRS module
"""
from ..utils import get, __airs_base_url__

def rel_humidty(layer, tilematrix, tilecol, tilerow, date, format="png", **kwargs):
    """
    Get Relative Humidity
    ::param layer: [string] AIRS_L2_RelativeHumidity_500hPa_Night

    """
    url = __airs_base_url__
    args = {
        "layer":layer,
        "tilematrixset":"EPSG4326_2km",
        "Service":"WMTS",
        "Request":"GetTile",
        "Version":"1.0.0",
        "Format":f"image/{format}",
        "TileMatrix":tilematrix,
        "TileCol":tilecol,
        "TileRow":tilerow,
        "TIME":date,
    }
    out = get(url, args, "image/png")
    return out

def co():
    """
    Get Carbon monoxide data
    """

def dust():
    """
    Get dust score
    """

def out_long_rad():
    """
    Get Outgoing Longwave Radiation
    """

def precipitation():
    """
    Get precipitation data
    """

def so2():
    """
    Get sulfur dioxide data
    """

def temp():
    """
    Get temperature data
    """

def h2o_vapour():
    """
    get water vapour data
    """