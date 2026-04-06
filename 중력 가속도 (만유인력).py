import numpy as np
import matplotlib.pyplot as plt

# 중력 상수 + 중심 질량 (단순화)
GM = 1.0

# 시간 설정
dt = 0.01 #시간 간격
steps = 2000 #시뮬레이션 스텝 수

#위치 배열 초기화
x = np.zeros(steps)
y = np.zeros(steps)

# 속도 배열 초기화
vx = np.zeros(steps)
vy = np.zeros(steps)

# 초기 위치: 오른쪽 1단위
x[0] = 1.0
y[0] = 0.0

# 초기 속도: 위쪽 방향, 원 궤도 속도
vx[0] = 0.0
vy[0] = 1.0

for i in range(steps -1):
    #현재 위치에서 중심까지 거리 계산
    r = np.sqrt(x[i]**2 + y[i]**2)

    #중력 가속도 계산 ( 방향 = 중심 )
    ax= -GM * x[i] / r**3
    ay= -GM * y[i] / r**3

    #속도 업데이트
    vx[i+1] = vx[i] + ax*dt
    vy[i+1] = vy[i] + ay*dt

    #위치 업데이트
    x[i+1] = x[i] + vx[i+1] * dt
    y[i+1] = y[i] + vy[i+1] * dt

    plt.figure(figsize=(6,6))
    plt.plot(0, 0, 'yo', label='Planet') # 행성 중심
    plt.plot(x, y, 'b-', label='Orbit') # 위성 궤도
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('2D Orbital Simulation (Euler)')
    plt.legend()
    plt.axis('equal')
    plt.grid(True)
    plt.show()
