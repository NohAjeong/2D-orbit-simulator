import numpy as np
import matplotlib.pyplot as plt

# 시간 배열 (초)
time = np.array([0, 1, 2, 3, 4, 5])

# 속도 배열 (m/s)
velocity = np.array([0, 3, 8, 15, 15, 10])

# 1️⃣ 속도 변화량과 시간 변화량
delta_v = velocity[1:] - velocity[:-1]   # Δv
delta_t = time[1:] - time[:-1]           # Δt

# 2️⃣ 가속도 배열
acceleration = delta_v / delta_t

# 3️⃣ 위치 배열 계산 (구간 이동 거리 누적)
x0 = 0
position = x0 + np.cumsum(velocity[:-1] * delta_t)  # 각 구간 이동거리 누적합

# 4️⃣ 출력
print("속도 배열:", velocity)
print("Δv 배열:", delta_v)
print("시간 간격 Δt:", delta_t)
print("가속도 배열:", acceleration)
print("위치 배열:", position)

# 5️⃣ 그래프 시각화
plt.figure(figsize=(8,5))
plt.plot(time, velocity, marker='o', label='속도 (m/s)')
plt.plot(time[:-1], acceleration, marker='x', label='가속도 (m/s²)')
plt.plot(time[:-1], position, marker='s', label='위치 (m)')
plt.xlabel('시간 (s)')
plt.ylabel('값')
plt.title('시간에 따른 속도, 가속도, 위치')
plt.legend()
plt.grid(True)
plt.show()
