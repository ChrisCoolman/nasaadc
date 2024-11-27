import math

pt=float(10.0)
gt=float(9.0)
losses=19.43
nr=0.55
greek_11=0.136363636
kb=-228.6
ts=float(22)
out=float(0)
DR=float(input("Enter DR "))
R=float(input("Enter R "))



def calculations(DR, R, out):
    # Ensure all inputs are valid for logarithmic calculations
    if nr * (((math.pi) + DR / greek_11) ** 2) <= 0:
        raise ValueError("Invalid input for nr calculation: must be positive.")
    
    if 4000 * (math.pi) * R / greek_11 <= 0:
        raise ValueError("Invalid input for R calculation: must be positive.")
    
    if ts <= 0:
        raise ValueError("Invalid input for ts: must be positive.")
    
    out = float((10 * (pt + gt - losses + 
                        10 * (math.log10(nr * (((math.pi) + DR / greek_11) ** 2)) - 
                        20 * (math.log10(4000 * (math.pi) * R / greek_11)) - kb - 
                        10 * (math.log10(ts))) / 10) / 1000))
    
    return out

out=(calculations(DR, R, out))
print(out)