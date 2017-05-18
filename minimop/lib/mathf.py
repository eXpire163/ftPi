import numpy as np


class Mathf(object):
    """Math heper """

    @staticmethod
    def lerp(xvalue, yvalue, delta):
        x_axis = [0, 1]
        y_axis = [xvalue, yvalue]
        result = np.interp(delta, x_axis, y_axis)
        return result
