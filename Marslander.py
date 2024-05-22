import marsatm
import math
import matplotlib.pyplot as plt

H = 0
T = 1
RHO = 2
A = 3

g_0 = -3.711 #m/s^2
v_e = 4400 #m/s
k_v = 0.05
v_y_ref = -2 #m/s
#positive UP, RIGHT
h = 2e4 #m
x = 0 #m
gamma = math.radians(-20) #rad
dt = 0.01 #s
v = 262 #m/s
v_x = v * math.cos(gamma)
v_y = v * math.sin(gamma)
m_zfw = 699 #kg
m_prop = 75 #kg
m = m_zfw + m_prop
m_dot = 0 #kg/s
t = 0
dat = []
t_steps = []

while (float(h) >= 0.3):
    t += dt
    
    atmData = marsatm.atmCalc(h)
    #drag component
    F_xd = 0.5 * 4.92 * pow(float(v_x), 2) * atmData[RHO] * (-1)
    F_yd = 0.5 * 4.92 * pow(float(v_y), 2) * atmData[RHO]
    #thrust component
    if(h < 2000 and h > 0.3 and m_prop >= 1e-3):
        m_dot = ((m * abs(g_0))/v_e) + k_v * (v_y_ref - v_y)
        if(m_dot > 5):
            m_dot = 5
        F_xt = m_dot * v_e * math.cos(gamma) * (-1)
        F_yt = m_dot * v_e * math.sin(gamma) * (-1)
        m_prop -= m_dot * dt
        m = m_zfw + m_prop
    else:
        F_xt = 0
        F_yt = 0
        m_dot = 0    
    
    a_x = (F_xd + F_xt)/m
    a_y = g_0 + (F_yd + F_yt)/m
    
    v_x += a_x * dt
    v_y += a_y * dt
    v = math.sqrt(pow(v_x,2) + pow(v_y,2))
    
    gamma = math.atan2(v_y,v_x)
    
    dat.append([h, x, v, m_dot, gamma])
    t_steps.append(t)
    
    h += v_y * dt
    x += v_x * dt
    
h_dat, x_dat, v_dat, m_dot_dat, gamma_dat = zip(*dat)  

plt.subplot(231)
plt.plot(x_dat, h_dat)
plt.title('Trajectory')

plt.subplot(232)
plt.plot(h_dat, v_dat)
plt.title('Speed')

plt.subplot(233)
plt.plot(t_steps, m_dot_dat)
plt.title('Mdot vs time')

plt.subplot(234)
plt.plot(t_steps, h_dat)
plt.title('Alt vs time')

plt.subplot(235)
plt.plot(t_steps, v_dat)
plt.title('Speed vs time')

plt.subplot(236)
plt.plot(t_steps, gamma_dat)
plt.title('Gamma vs time')

plt.show()