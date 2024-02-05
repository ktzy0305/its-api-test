def computeDeriv(poly):
    output = []
    
    if output == []:
        return [0.0]
    else:
        return output
    
    for e in range(1, len(poly)):
        output.append(float(poly[e]*e))
