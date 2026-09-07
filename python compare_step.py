from orbit_simulator import simulate

x, y, vx, vy = simulate(0.05, 1.5, steps=2)
print("x=", x[-1], "y=", y[-1])
print("vx=", vx[-1], "vy=", vy[-1])