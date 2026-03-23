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

## 실험 결과 및 분석

- 실험 목적: dt 변화에 따른 궤도 안정성과 에너지 보존 확인
- 실험 조건: vy = 1.0, dt = 0.01, 0.05, 0.1

### 결과 요약
- dt=0.01: 안정, 에너지 일정
- dt=0.05: 에너지 약간 흔들림, 궤도 거의 겹침
- dt=0.1: 에너지 오차 큼, 궤도 불안정

### 궤도 그래프
![Orbit dt=0.01](orbit_dt_0.01.png)
![Orbit dt=0.05](orbit_dt_0.05.png)
![Orbit dt=0.1](orbit_dt_0.1.png)

### 에너지 그래프 (vy=1.0)
![Energy dt=0.01](energy_dt_0.01.png)
![Energy dt=0.05](energy_dt_0.05.png)
![Energy dt=0.1](energy_dt_0.1.png)

### 결론
- Leapfrog 방법은 안정적이지만, dt가 커지면 정확도가 감소함
- 짧은 시간 스케일에서는 궤도 변화는 크지 않음
