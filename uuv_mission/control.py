# Defining controller function

def controller(t, positions, references, kp, kd):
    # Calling current output, reference and error values
    y1 = positions[t][1]
    r1 = references[t]
    e1 = r1 - y1

    # Calling previous output, reference and error values, error equals zero if t=0
    if t == 0:
        e0 = 0
    else:
        y0 = positions[t-1][1]
        r0 = references[t-1]
        e0 = r0 - y0

    # Controller action expression
    u = (kp*e1) + kd * (e1 - e0)
    return u
        
