"""
AIRS module
"""
from ..utils import get, __airs_base_url__

def rel_humidty(layer, tilematrix, tilecol, tilerow, date, format="png", **kwargs):
    """
    Get Relative Humidity
    :param layer: [string] choose between
        AIRS_L2_RelativeHumidity_500hPa_Night
        AIRS_L2_RelativeHumidity_500hPa_Day
        AIRS_L2_RelativeHumidity_700hPa_Night
        AIRS_L2_RelativeHumidity_500hPa_Day
        AIRS_L2_RelativeHumidity_850hPa_Night
        AIRS_L2_RelativeHumidity_850hPa_Day
        AIRS_L2_Surface_Relative_Humidity_Day
        AIRS_L2_Surface_Relative_Humidity_Night

    :param tilematrix: [integer]
    :param tilerow: [integer]
    :param tilecol: [integer]
    :param date: [date string] format YYYY-MM-DD
    :param format: [string] png/jpeg formats

    Usage::

    # fetch tile as image/png
    response = airs.rel_humidty(
                layer="AIRS_L2_RelativeHumidity_500hPa_Night", 
                tilecol=1,
                tilematrix=3, 
                tilerow=1, 
                date="2011-10-08")
    with open('img.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
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

def co(layer, tilematrix, tilecol, tilerow, date, format="png", **kwargs):
    """
    Get Carbon monoxide data
    :param layer: [string]
        AIRS_L2_Carbon_Monoxide_500hPa_Volume_Mixing_Ratio_Day
        AIRS_L2_Carbon_Monoxide_500hPa_Volume_Mixing_Ratio_Night
    :param tilematrix: [integer]
    :param tilerow: [integer]
    :param tilecol: [integer]
    :param date: [date string] format YYYY-MM-DD
    :param format: [string] png/jpeg formats

    Usage::

    # fetch tile as image/png
    response = airs.co(
                layer="AIRS_L2_Carbon_Monoxide_500hPa_Volume_Mixing_Ratio_Day", 
                tilecol=1,
                tilematrix=3, 
                tilerow=1, 
                date="2011-10-08")
    with open('img.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
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
    out = get(url, args, 'image/png')
    return out

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