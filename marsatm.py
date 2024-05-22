H = 0
T = 1
RHO = 2
A = 3

def interpolate(x, x_1, x_2, y_1, y_2):
    k = (x-x_1)/(x_2-x_1)
    y = (1-k) * y_1 + k * y_2
    return y

def marsinit():
    atm_data = []
    with open('marsatm.txt', 'r') as atm:
        next(atm)
        next(atm)
        for line in atm:
            # Strip newline characters and split the line by whitespace
            values = line.strip().split()
            # Append the list of values to the main data list
            atm_data.append(values)
    return atm_data

def atmCalc(alt):
    ref_atm = marsinit()
    index = 0
    alt = alt/1000
    atmData = []
    atmData.append(alt)
    while float(alt) >= float(ref_atm[index][H]):
        index += 1
    for i in range(1,4):   
        atmData.append(interpolate(float(alt), float(ref_atm[index][H]),  float(ref_atm[index-1][H]), float(ref_atm[index][i]), float(ref_atm[index-1][i])))
    return atmData