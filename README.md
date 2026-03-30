# 2D-orbit-simulator
# 2D Orbital Mechanics Simulator

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
python leapfrog.py
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
