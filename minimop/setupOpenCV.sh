# warning !!!! this is just a test
# guide from https://tutorials-raspberrypi.de/opencv-auf-dem-raspberry-pi-installieren/

sudo apt-get install build-essential -y
sudo apt-get install git -y
sudo apt-get install cmake -y
sudo apt-get install pkg-config -y
sudo apt-get install libjpeg8-dev -y
sudo apt-get install libtiff4-dev -y
sudo apt-get install libjasper-dev -y
sudo apt-get install libpng12-dev -y
sudo apt-get install libavcodec-dev -y
sudo apt-get install libavformat-dev -y
sudo apt-get install libswscale-dev -y
sudo apt-get install libv4l-dev -y
sudo apt-get install libgtk2.0-dev -y
sudo apt-get install libatlas-base-dev -y
sudo apt-get install gfortran -y


git clone https://github.com/Itseez/opencv.git && cd opencv &&git checkout 3.0.0
sudo apt-get install python2.7-dev -y


pip install numpy


cd opencv && mkdir build && cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
 -D CMAKE_INSTALL_PREFIX=/usr/local \
 -D INSTALL_PYTHON_EXAMPLES=ON \
 -D INSTALL_C_EXAMPLES=ON \
 -D OPENCV_EXTRA_MODULES_PATH=opencv_contrib/modules \
 -D BUILD_EXAMPLES=ON ..
 
echo "logging to ~/makelog.log (tail -f for access)"
make > ~/makelog.log


#sudo make install && sudo ldconfig
#import cv2
#cv2.__version__