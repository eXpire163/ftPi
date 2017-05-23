import time
from lib.mathf import Mathf




class Eyes(object):
    def __init__(self):
        self.reset_vars()
        
    def reset_vars(self):
        self._pos = [64, 20]
        self._space = 5
        self._color = "white"

        self._size_left = [24, 24]
        self._pos_left = [self._pos[0] - self._size_left[0] - self._space, self._pos[1]]

        self._size_right = [24, 24]
        self._pos_right = [self._pos[0] + self._space, self._pos[1]]

        self._starttime = 0
        self._duration = 0
        self._actionstep = 0
        self._action = "non"


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
            self.actionzwinkern()
        if self._action == "blinzeln":
            self.actionblinzeln()

    def actionzwinkern(self):
        current_step = (time.time()-self._starttime)/self._duration
        if(current_step < 0.5):
            self._size_left[1] = Mathf.lerp(24, 8, current_step*2)
            self._size_left[0] = Mathf.lerp(24, 30, current_step*2)
        elif(current_step < 1):
            self._size_left[1] = Mathf.lerp(8, 24, (current_step-0.5)*2)
            self._size_left[0] = Mathf.lerp(30, 24, (current_step-0.5)*2)
        else:
            self.reset_vars()
        #print("action: {} - current_step {} {} ".format(self._action, current_step, self._size_left))

    def actionblinzeln(self):
        current_step = (time.time()-self._starttime)/self._duration

        step_duration_0 = 0.0
        step_duration_1 = 0.5
        step_duration_2 = 1.0
        
        totalSteps = 2
        

        if(current_step < 0.5):
            previos_duration = step_duration_0
            step_pos = current_step*totalSteps
            self._size_left[1] = Mathf.smoothstep(24, 8, step_pos)
            self._size_left[0] = Mathf.smoothstep(24, 30, step_pos)
            self._size_right[1] = Mathf.smoothstep(24, 8, step_pos)
            self._size_right[0] = Mathf.smoothstep(24, 30, step_pos)
        elif(current_step < 1):
            previos_duration = step_duration_1
            step_pos = (current_step-previos_duration)*totalSteps
            self._size_left[1] = Mathf.smoothstep(8, 24, step_pos)
            self._size_left[0] = Mathf.smoothstep(30, 24, step_pos)
            self._size_right[1] = Mathf.smoothstep(8, 24, step_pos)
            self._size_right[0] = Mathf.smoothstep(30, 24, step_pos)
        else:
            self.reset_vars()
        #print("action: {} - current_step {} {} ".format(self._action, current_step, self._size_left))



    def draw(self, canvas):
        #left
        x1 = self._pos_left[0]
        y1 = self._pos_left[1]
        x2 = self._pos_left[0] + self._size_left[0]
        y2 = self._pos_left[1] + self._size_left[1]
        print("left {} {} {} {}".format(x1,y1,x2,y2))
        canvas.rectangle((x1, y1, x2, y2), fill=self._color)
        #right
        xx1 = self._pos_right[0]
        yy1 = self._pos_right[1]
        xx2 = self._pos_right[0] + self._size_right[0]
        yy2 = self._pos_right[1] + self._size_right[1]
        canvas.rectangle((xx1, yy1, xx2, yy2), fill=self._color)
        #print("righ {} {} {} {}".format(x1,y1,x2,y2))
        