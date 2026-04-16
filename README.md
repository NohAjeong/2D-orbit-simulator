# 2D-orbit-simulator
# 2D Orbital Mechanics Simulator

이 프로젝트는 중력 법칙을 기반으로 만든 2D 궤도 시뮬레이터입니다.
물체의 위치와 속도를 바탕으로 시간에 따른 궤도 변화를 계산하고 시각화합니다.
항공우주 분야에 대한 흥미와 관심으로 시작했으며, 단순한 이론 이해를 넘어 궤도 운동을 직접 구현해보고자 했습니다.  
특히 물체의 위치와 속도에 따라 궤도가 어떻게 변화하는지 코드로 확인하고, 이를 시각화하는 것을 목표로 개발했습니다.

## 개요
- 뉴턴 만유인력 기반 2D 궤도 시뮬레이션
- Euler와 Leapfrog 적분법 비교
- 궤도 안정성 및 시간 간격(dt) 민감도 실험

## 주요 기능
1. 원/타원/탈출 궤도 시뮬레이션
2. Leapfrog integrator를 사용한 수치 안정성 개선
3. 속도(vy)와 시간 간격(dt) 변경 실험
4. 궤도 시각화 및 에너지 계산

## 설치 및 실행 방법
```bash
git clone <repo-url>
pip install numpy matplotlib
python orbit_simulator.py
```
## 프로젝트 소개

- 뉴턴 만유인력 기반 2D 궤도 시뮬레이션
- Leapfrog 적분법으로 수치 안정성 향상
- 속도(vy)와 시간 간격(dt)를 바꿔가며 궤도와 에너지 변화 분석
- 코드 구조화: `simulate()`, `compute_energy()`, `plot_orbit()`, `plot_energy()` 함수

## 주요 기능
1. 원, 타원, 탈출 궤도 시뮬레이션
2. Leapfrog integrator를 사용한 수치 안정성 개선
3. 속도(vy)와 시간 간격(dt) 변경 실험
4. 궤도 및 에너지 시각화

## 실험 결과 및 분석

- 실험 목적: 시간 간격(dt) 변화에 따른 초기 속도(vy)에 따른 궤도 안정성과 에너지 보존 확인
- 실험 조건: dt = 0.05, vy = 0.8, 1.0, 1.2, 1.5

### 결과 요약
속도별 특징:
- vy=0.8: 타원 궤도, 에너지 거의 일정, 안정적
- vy=1.0: 원 궤도, 기준 속도, 에너지 일정
- vy=1.2: 타원 궤도, 에너지 약간 증가, 궤도 점프 길어짐 
- vy=1.5: 탈출 궤도, 에너지 증가, 궤도 벗어남 

### 궤도 그래프
![Orbit dt=0.01](orbit_dt_0.01.png)
![Orbit dt=0.05](orbit_dt_0.05.png)
![Orbit dt=0.1](orbit_dt_0.1.png)
![Orbit dt=0.05](orbit_dt_0.05.png)

### 에너지 그래프 (vy=1.0)
![Energy dt=0.01](energy_dt_0.01.png)
![Energy dt=0.05](energy_dt_0.05.png)
![Energy dt=0.1](energy_dt_0.1.png)
![Energy dt=0.05](energy_dt_0.05.png)

### 결론
- Leapfrog 방법은 안정적이며 에너지 보존이 뛰어나지만, dt가 커지면 정확도가 감소
- 속도가 기준 속도에서 벗어나면 궤도가 타원화 또는 탈출 궤도로 변함
- 시뮬레이션과 그래프 시각화를 통해 물리적 직관과 수치 안정성을 동시에 확인 가능
