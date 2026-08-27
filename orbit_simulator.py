import numpy as np
import matplotlib.pyplot as plt
import os

GM = 1.0

def simulate(dt, vy_init, steps = 10000): # --- 함수 정의: 시뮬레이션 ---
    # dt = 시간 간격 , vy_init = 초기 y 방향 속도 , x,y,vx,vy = 시간에 따른 위치와 속도 배열
    # 위치, 속도, 에너지 배열 초기화 
    
    x = np.zeros(steps)
    y = np.zeros(steps)
    vx = np.zeros(steps)
    vy = np.zeros(steps)

    # 초기 위치 x=1.0, y=0.0
    # 초기 속도 vy_init: 속도에 따라 타원, 원, 탈출 궤도 결정
    x[0], y[0] = 1.0, 0.0
    vx[0], vy[0] = 0.0, vy_init

    # 초기 r 계산 (루프 밖에서 1번만) 초기 거리 
    r = np.sqrt(x[0]**2 + y[0]**2)

    # leapfrog integration
    for i in range(steps - 1):
        # 중력 가속도 계산: a = -GM/r^2 방향, 항공/우주 궤도에서 중심 천체의 인력 모델링
        ax = -GM * x[i] / r**3
        ay = -GM * y[i] / r**3

        # velocity half-step update
        # 현재 위치에서 속도를 반 스텝만큼 먼저 업데이트 -> 에너지 보존에 유리
        vx_half = vx[i] + ax * dt / 2 
        vy_half = vy[i] + ay * dt / 2

        # position update
        # 그 속도로 위치 한 스텝 이동
        x[i + 1] = x[i] + vx_half * dt # 위치 한 걸음 이동 (다음 위치 계산)
        y[i + 1] = y[i] + vy_half * dt 

        # acceleration update at new position
        # 새 위치에서 가속도 계산 ('다음 위치'의 거리)
        r_new = np.sqrt(x[i + 1]**2 + y[i + 1]**2) # 다음 위치에서 r 계산
        ax_new = -GM * x[i + 1] / r_new**3 # 새 위치에서 가속도 계산
        ay_new = -GM * y[i + 1] / r_new**3

        # velocity full-step update
        # 속도 반 스텝 더해 전체 스텝 완성
        vx[i + 1] = vx_half + ax_new * dt / 2 # 속도 다음 반 걸음 마무리
        vy[i + 1] = vy_half + ay_new * dt / 2

        # ****** 핵심 : r 업데이트 ****** 시간 흐름 따라 r 업데이트
        r = r_new

    return x, y, vx, vy
    
def compute_energy(x, y, vx, vy): # --- 에너지 계산 함수 --- (각 시간 스텝에서의 총 에너지 계산)
    r = np.sqrt(x**2 + y**2) # 현재 i번째 위치에서의 거리
    v2 = vx**2 + vy**2
    return 0.5 * v2 - GM / r  # 에너지 계산 (1/2 m v^2 - GM/r)

def plot_orbit(x, y, color, label): # --- 궤적 그리기 함수 --- (행성 궤적과 시작점 표시)
    plt.plot(x, y, color=color, label=label, linewidth=2) # 궤적
    plt.scatter(x[0], y[0], color=color, s=30) # 시작점 표시    

def plot_energy(energy, label): # --- 에너지 그래프 함수 --- 
    # ✅ figure/show 제거 -> 한 번만 생성
    plt.plot(energy, label=label)

# --- 메인 코드 ---
if __name__ == "__main__":
    velocities = [0.8, 1.0, 1.2, 1.5]
    dt = 0.05
    current_folder = os.path.dirname(os.path.abspath(__file__))
    colors = ["#1f77b4", "#2ca02c", "#ff7f0e", "#d62728"]

    plt.style.use("seaborn-v0_8") # 그래프 전체의 기본 디자인 테마를 바꾸는 것

    # --- 시뮬레이션 실행 ---
    results = []

    for i, vy_init in enumerate(velocities):
        result = simulate(dt, vy_init)
        results.append(result)

    # =========================
    # 1️⃣ 전체 궤적
    # =========================
    plt.figure(figsize=(8, 8))

    for i, vy_init in enumerate(velocities):
        x, y, vx, vy = results[i]
        plot_orbit(x, y, color=colors[i], label=f"vy={vy_init}")

    # 중심 질량 (태양 느낌) / 그래프가 (0,0)을 중심 기준으로 인식
    plt.scatter(0,0, color="black", s=80, label="Center")
    plt.title("Orbital Trajectories with Different Initial Velocities", fontsize=14)
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.legend(frameon=True)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.axis("equal")
    plt.tight_layout() # 여백 자동 조정 (불필요한 공간 제거)
    plt.savefig(os.path.join(current_folder, f"orbit_dt_{dt}.png"))
    plt.show()

    # =========================
    # 2️⃣ 에너지 그래프
    # =========================
    plt.figure(figsize=(8, 6)) # 👉 한 번만 생성

    for i, vy_init in enumerate(velocities):
        x, y, vx, vy = results[i]
        energy = compute_energy(x, y, vx, vy)
        plot_energy(energy, label=f"vy={vy_init}")


    plt.title("Total Energy over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Energy")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(current_folder, f"energy_dt_{dt}.png"))
    plt.show()

    # vy=0.8 타원 궤도 / 에너지 거의 일정 / 안정적
    # vy=1.0 원 궤도 / 일정 / 기준 속도 
    # vy=1.2 타원 궤도 / 에너지 약간 증가 / 더 길게 점프 
    # vy=1.5 탈출 궤도 / 에너지 증가 / 궤도 벗어남