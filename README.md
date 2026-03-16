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
