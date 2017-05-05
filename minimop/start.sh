pkill -f display.py
pkill -f sound.py
pkill -f motion.py
python display.py &
python sound.py &
python motion.py &
