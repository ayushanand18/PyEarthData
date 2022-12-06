"""
Fetching NASA/POWER CERES/MERRA2 Native Resolution Daily Data
"""

from .utils import get

def get_temp(longitude, latitude, start, end, **kwargs):
    """
    Fetch temperature data at a specific date and (lat, lon) pair
    
    :param longitude: [Float] Longitude e.g. 77.0000
    :param latitude: [Float] Latitude
    :param start: [Integer] Start date. format YYYYMMDD
    :param end: [Integer] End Date. format YYYYMMDD

    Usage::
    from MarinePySim import power
    res = power.get_temp(77,22,20141201,20141205)
    print(res)
    print(res["geometry"])
    """
    args = {
        "parameters":"QV2M,RH2M,PRECTOTCORR",
        "community":"RE",
        "longitude":longitude,
        "latitude":latitude,
        "start":start,
        "end":end,
        "format":"JSON",
        "user":"DAV",
    }
    url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    out = get(url, args, "application/json", **kwargs)
    
    return out.json()