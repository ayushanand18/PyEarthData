# PyEarthData
[![pypi](https://img.shields.io/pypi/v/PyEarthData.svg)](https://pypi.python.org/pypi/PyEarthData) [![docs](https://github.com/ayushanand18/PyEarthData/actions/workflows/deploy-docs.yml/badge.svg)](https://ayushanand18.github.io/PyEarthData)

Python Package for grabbing Earth surface and atmospheric data.

[Source on GitHub at ayushanand18/PyEarthData](https://github.com/ayushanand18/PyEarthData)

## Introduction
PyEarthData is an easy-to-use python package that helps users fetch data remote sensing data about Earth's surface and atmospheric data. It allows users to fetch historic data about concentration of gases in atmosphere, relative humidity, surface temperature, etc from sensors aboard NASA's satellites.

## Main Features
+ Get historic and near real-time (NRT) data of Earth's surface and Atmosphere directly from [AIRS](https://airs.jpl.nasa.gov/) equipment aboard NASA's [aqua](https://aqua.nasa.gov/) satellite and combine it with any GIS tools easily using python. Query for concentration of gases in atmosphere, relative humidity, outgoing radiation, etc.
+ Get historic as well as near real-time (NRT) data of Earth Surface Temperature from NASA's POWER (Prediction of Worldwide Energy Resources).

## Installation
### Installation from PyPI
```python
pip install PyEarthData
```

### Install latest development version from GitHub
```python
pip install git+git://github.com/ayushanand18/pyearthdata.git#egg=pyearthdata
```

Install editable dev version from github for local development. System prerequisites: python3, conda
```python
# fetch code
git clone git@github.com:ayushanand18/pyearthdata.git
cd PyEarthData
# install
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
python -m pip install -e .
```

## Documentation
The official documentation is hosted on GitHub Pages https://ayushanand18.github.io/PyEarthData.

## Modules

### `airs`
AIRS module: Get Data directly from AIRS aboard NASA’s Aqua Satellite
```python
from pyearthdata import airs
```

### `power`
POWER module: Fetching NASA/POWER CERES/MERRA2 Native Resolution Daily Data
```python
from pyearthdata import power
```

## Meta
+ License: MIT, see [LICENSE file](https://github.com/ayushanand18/PyEarthData/blob/main/LICENSE)
+ Help make this project even more useful! Please read the [contribute on GitHub](https://github.com/ayushanand18).

## Further Reading
+ For issues with the package itself, feel free to open an issue on GitHub!

----

```javascript
const package = {
    "name" = "PyEarthData",
    "author" = "Ayush Anand",
} 
Made with ❤️ in Python
```
