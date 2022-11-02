def Lerp(a, b, t):
    return (1.0f - t) * a + b * t

def InvLerp(a, b, v):
    return (v - a) / (b - a)

def Remap(iMin, iMax, oMin, oMax, v):
    t = InvLerp(iMin, iMax, v)
    return Lerp(oMin, oMax, t)
