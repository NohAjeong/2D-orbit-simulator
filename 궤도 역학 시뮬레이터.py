# ---- 코드 시작 ----
import numpy as np
import matplotlib.pyplot as plt

# ---- 설정 ----
GM = 1.0
dt = 0.01
steps = 2000

x = np.zeros(steps) #numpy 배열을 만들면서 모든 값을 0으로 채우는 함수 
y = np.zeros(steps) #2000개의 시간 칸을 미리 만들어 놓는다
vx = np.zeros(steps)
vy = np.zeros(steps)
E = np.zeros(steps)

# 초기 위치/속도 (원 궤도 기준)
x[0], y[0] = 1.0, 0.0
vx[0], vy[0] = 0.0, 1.0

# ---- Euler 통합 ----
for i in range(steps-1):
    r = np.sqrt(x[i]**2 + y[i]**2)
    ax = -GM * x[i] / r**3
    ay = -GM * y[i] / r**3
    vx[i+1] = vx[i] + ax*dt         
    vy[i+1] = vy[i] + ay*dt
    x[i+1] = x[i] + vx[i+1]*dt  
    y[i+1] = y[i] + vy[i+1]*dt

for i in range(steps):
    r = np.sqrt(x[i]**2 + y[i]**2)
    v2 = vx[i]**2 + vy[i]**2
    E[i] = 0.5*v2 - GM/r
    
# ---- 시각화 ----
plt.figure(figsize=(6,6))
plt.plot(0,0,'yo',label='Planet')
plt.plot(x,y,'b-',label='Orbit')
plt.axis('equal'); plt.grid(True); plt.legend(); plt.show()

plt.figure()
plt.plot(E)
plt.title("Total Energy")
plt.grid()
plt.show()
