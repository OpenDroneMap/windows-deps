# windows-deps
Prebuilt Windows dependencies for ODM

Python dependencies are downloaded from https://www.lfd.uci.edu/~gohlke/pythonlibs/

To download them, run `python3 get_deps.py`. To change versions, change the values of `gdal_wheel_url`, `fiona_wheel_url`, `rasterio_wheel_url`, and `python_zip` in `get_deps.py`.

The github workflow `build_python_wheels.yaml` creates the python dependencies.
The github workflow `build_vcpkg_env.yaml` creates the vcpkg dependencies.
