# Defining controller function

def controller(t, positions, references):
    y1 = positions[t][1]
    r1 = references[t]
    e1 = r1 - y1


    if t == 0:
        e0 = 0
    else:
        y0 = positions[t-1][1]
        r0 = references[t-1]
        e0 = r0 - y0

    u = (0.15*e1) + 0.6 * (e1 - e0)
    return u
        
