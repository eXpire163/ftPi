import numpy as np


class Mathf(object):
    """Math heper """

    @staticmethod
    def lerp(xvalue, yvalue, delta):
        xp = [0, 1] 
        fp = [xvalue, yvalue]
        tt = np.interp(delta, xp, fp)
        return tt

    @staticmethod
    def lerp2(xvalue,yvalue,delta):
        xp = [0,1]
        fp = [xvalue,yvalue]
        tt = np.interp(delta,xp,fp)
        return tt


xt = Mathf.lerp(0, 10, .5)
print xt
