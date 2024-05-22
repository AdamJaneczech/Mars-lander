g_0 = 3.711
atm_data = []

H = 0
T = 1
RHO = 2
A = 3

def interpolate(x, x_1, x_2, y_1, y_2):
    print(x,x_1,x_2,y_1,y_2)
    k = (x-x_1)/(x_2-x_1)
    y = (1-k) * y_1 + k * y_2
    return y

def marsinit():
    print()

def marsatm(alt, marstable):
    index = 0
    atmCalc = []
    atmCalc.append(alt)
    while float(alt) >= float(marstable[index][H]):
        index += 1
    for i in range(1,4):   
        atmCalc.append(interpolate(float(alt), float(marstable[index][i]), float(marstable[index-1][i]), float(marstable[index][H]), float(marstable[index-1][H])))
    return atmCalc
    
with open('marsatm.txt', 'r') as atm:
    next(atm)
    next(atm)
    for line in atm:
        # Strip newline characters and split the line by whitespace
        values = line.strip().split()
        # Append the list of values to the main data list
        atm_data.append(values)
    
    #print(atm_data)
    print(marsatm(input('Enter h'), atm_data))