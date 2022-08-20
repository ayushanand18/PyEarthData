"""
AIRS module
"""
from ..utils import get, __airs_base_url__

def rel_humidity(layer, tilematrix, tilecol, tilerow, date, format="png", **kwargs):
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
    :param layer: [string] choose between
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

def dust(layer, tilematrix, tilecol, tilerow, date, format="png", **kwargs):
    """
    Get dust score
    :param layer: [string]
        AIRS_L2_Dust_Score_Day
        AIRS_L2_Dust_Score_Night
    :param tilematrix: [integer]
    :param tilerow: [integer]
    :param tilecol: [integer]
    :param date: [date string] format YYYY-MM-DD
    :param format: [string] png/jpeg formats

    Usage::

    # fetch tile as image/png
    response = airs.dust(
                layer="AIRS_L2_Dust_Score_Day", 
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

def out_long_rad(layer, tilematrix, tilecol, tilerow, date, format="png", **kwargs):
    """
    Get Outgoing Longwave Radiation
    :param layer: [string]
        AIRS_L3_All_Sky_Outgoing_Longwave_Radiation_Daily_Day
        AIRS_L3_All_Sky_Outgoing_Longwave_Radiation_Daily_Night
    :param tilematrix: [integer]
    :param tilerow: [integer]
    :param tilecol: [integer]
    :param date: [date string] format YYYY-MM-DD
    :param format: [string] png/jpeg formats

    Usage::

    # fetch tile as image/png
    response = airs.out_long_rad(
                layer="AIRS_L3_All_Sky_Outgoing_Longwave_Radiation_Daily_Day", 
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

def precipitation(layer, tilematrix, tilecol, tilerow, date, format="png", **kwargs):
    """
    Get precipitation data
    :param layer: [string]
        AIRS_Precipitation_Day
        AIRS_Precipitation_Night
    :param tilematrix: [integer]
    :param tilerow: [integer]
    :param tilecol: [integer]
    :param date: [date string] format YYYY-MM-DD
    :param format: [string] png/jpeg formats

    Usage::

    # fetch tile as image/png
    response = airs.precipitation(
                layer="AIRS_Precipitation_Day", 
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

def so2(layer, tilematrix, tilecol, tilerow, date, format="png", **kwargs):
    """
    Get sulfur dioxide data
    :param layer: [string]
        AIRS_L2_Sulfur_Dioxide_Brightness_Temperature_Difference_Day
        AIRS_L2_Sulfur_Dioxide_Brightness_Temperature_Difference_Night
        AIRS_Prata_SO2_Index_Day
        AIRS_Prata_SO2_Index_Night
    :param tilematrix: [integer]
    :param tilerow: [integer]
    :param tilecol: [integer]
    :param date: [date string] format YYYY-MM-DD
    :param format: [string] png/jpeg formats

    Usage::

    # fetch tile as image/png
    response = airs.so2(
                layer="AIRS_L2_Sulfur_Dioxide_Brightness_Temperature_Difference_Day", 
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

def temp(layer, tilematrix, tilecol, tilerow, date, format="png", **kwargs):
    """
    Get temperature data
    :param layer: [string]
        AIRS_L2_Surface_Air_Temperature_Day
        AIRS_L2_Surface_Air_Temperature_Night
        AIRS_L2_Surface_Skin_Temperature_Day
        AIRS_L2_Surface_Skin_Temperature_Night
        AIRS_L2_Temperature_500hPa_Day
        AIRS_L2_Temperature_500hPa_Night
        AIRS_L2_Temperature_700hPa_Day
        AIRS_L2_Temperature_700hPa_Night
        AIRS_L2_Temperature_850hPa_Day
        AIRS_L2_Temperature_850hPa_Night
    :param tilematrix: [integer]
    :param tilerow: [integer]
    :param tilecol: [integer]
    :param date: [date string] format YYYY-MM-DD
    :param format: [string] png/jpeg formats

    Usage::

    # fetch tile as image/png
    response = airs.temp(
                layer="AIRS_L2_Surface_Air_Temperature_Day", 
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

def h2o_vapour(tilematrix, tilecol, tilerow, date, format="png", layer="AMSR2_Columnar_Water_Vapor_Day", **kwargs):
    """
    get water vapour data
    :param layer: [string]
        AMSR2_Columnar_Water_Vapor_Day
    :param tilematrix: [integer]
    :param tilerow: [integer]
    :param tilecol: [integer]
    :param date: [date string] format YYYY-MM-DD
    :param format: [string] png/jpeg formats

    Usage::

    # fetch tile as image/png
    response = airs.h2o_vapour(
                layer="AMSR2_Columnar_Water_Vapor_Day", 
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

def map_underlay(tilematrix, tilecol, tilerow, date, format="jpeg", layer="BlueMarble_NextGeneration", **kwargs):
    """
    Get earth satellite view underlaying the data
    
    :param tilematrix: [integer]
    :param tilerow: [integer]
    :param tilecol: [integer]
    :param date: [date string] format YYYY-MM-DD
    :param format: [string] png/jpeg formats

    Usage::
    
    # fetch background earth view tile as image/jpeg
    response = airs.map_underlay(
                tilematrix=2,
                tilecol=2,
                tilerow=0, 
                date="2011-10-08")
    with open('img.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    """
    url = __airs_base_url__
    args = {
        "layer":layer,
        "tilematrixset":"EPSG4326_500m",
        "Service":"WMTS",
        "Request":"GetTile",
        "Version":"1.0.0",
        "Format":f"image/{format}",
        "TileMatrix":tilematrix,
        "TileCol":tilecol,
        "TileRow":tilerow,
        "TIME":date,
    }
    out = get(url, args, "image/jpeg")
    return out
