import time
from lib.mathf import Mathf




class Eyes(object):
    def __init__(self):
        self.reset_vars()
        self._starttime = 0
        self._duration = 0
        self._actionstep = 0
        self._action = "non"

    def reset_vars(self):
        self._pos = [64, 20]
        self._space = 5
        self._color = "white"

        self._size_left = [24, 24]
        self._pos_left = [self._pos[0] - self._size_left[0] - self._space, self._pos[1]]

        self._size_right = [24, 24]
        self._pos_right = [self._pos[0] + self._space, self._pos[1]]

    def set_action(self, action, duration):
        self.reset_vars()
        self._action = action
        self._duration = duration
        self._starttime = time.time()

    def get_status(self):
        return "Current action: {}".format(self._action)

    def update_pos(self):
        """updates positions"""
        if self._action == "zwinkern":
            print(self._action)
            self.actionzwinkern()

    def actionzwinkern(self):
        current_step = (time.time()-self._starttime)/self._duration
        if(current_step < 0.5):
            self._size_left[0] = Mathf.lerp(24, 8, current_step/2)
        elif(current_step < 1):
            self._size_left[1] = Mathf.lerp(8, 24, (current_step/2)+0.5)
        else:
            self.reset_vars()


    def draw(self, canvas):
        #left
        canvas.rectangle((self._pos_left, self._pos_left+self._size_left), fill=self._color)
        #right
        canvas.rectangle((self._pos_right, self._pos_right+self._size_right), fill=self._color)
