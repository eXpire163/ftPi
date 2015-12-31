#sudo service motion stop

sudo nice -n -3 mjpg_streamer -i "/usr/local/lib/input_uvc.so -d /dev/video0 -r 320x240 -f 15 -q 85  -n" -o "/usr/local/lib/output_http.so -n -w /usr/local/www -p 8883"
