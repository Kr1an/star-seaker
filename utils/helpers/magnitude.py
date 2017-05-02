import math


def _pogson_calculation_specific(E1, stars):
    E1 = stars[0]
    array_magnitude = []
    for i in xrange(len(stars)):
        delta_m = math.log10(float(E1) / stars[i]) / 0.4
        array_magnitude.append(delta_m)
    return array_magnitude

def pogson_calculation(yellow, blue):
    E1 = yellow[0]
    array_delta_m_blue = _pogson_calculation_specific(E1, blue)
    array_delta_m_yellow = _pogson_calculation_specific(E1, yellow)
    return [array_delta_m_blue, array_delta_m_yellow]
