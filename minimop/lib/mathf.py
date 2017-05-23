import numpy as np


class Mathf(object):
    """Math heper """

    @staticmethod
    def lerp(xvalue, yvalue, delta):
        x_axis = [0, 1]
        y_axis = [xvalue, yvalue]
        result = np.interp(delta, x_axis, y_axis)
        return result

    @staticmethod
    def smoothstep(edge0, edge1, x):    
        # Scale, bias and saturate x to 0..1 range
        x = Mathf.clamp((x - edge0)/(edge1 - edge0), 0.0, 1.0)
        # Evaluate polynomial
        return x*x*(3 - 2*x)


    @staticmethod
    def clamp(x, lowerlimit, upperlimit):        
        if (x < lowerlimit):
            x = lowerlimit
        if (x > upperlimit):
            x = upperlimit
        return x

