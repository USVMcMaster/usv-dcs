# Code for Intel® RealSense™ Python Wrapper

### How to import RealSense?
```python
git clone https://github.com/IntelRealSense/librealsense
cd librealsense
mkdir build
cd build

cmake ../ -DBUILD_PYTHON_BINDINGS=TRUE

make -j4

sudo make install

export PYTHONPATH=$PYTHONPATH:/usr/local/lib
```

### How to run scripts with the import?
If it all goes without errors, you should be able to find the pyrealsense2.<arch info>.so under build/wrappers/python (actually 3 files with the same name and extensions .so, .so.2, .so.2.8.1).
Now the easiest way to use it is run python from that folder and import pyrealsense2

### How to import cv2?
First do run these commands inside Terminal/CMD:

```python
conda update anaconda-navigator  
conda update navigator-updater
```

if you are on linux you can do :
```python
pip install opencv-python

or

conda install opencv

```
