import numpy as np
from orbit_simulator import simulate, compute_energy

dt_values = [0.05, 0.10, 0.15, 0.20]
test_vy = 1.5
energy_ranges = []
changes = []
for dt in dt_values:
    x, y, vx, vy = simulate(dt, test_vy)
    assert len(x) == len(y) == len(vx) == len(vy)
    assert x[0] == 1.0
    assert y[0] == 0.0
    assert vx[0] == 0.0
    assert vy[0] == test_vy
    assert y[1] != 0.0

    energy = compute_energy(x, y, vx, vy)
    max_energy = max(energy)
    min_energy = min(energy)

    energy_range = max_energy - min_energy
    initial_energy = energy[0]
    change = energy_range / abs(initial_energy) * 100
    changes.append(change)
    energy_ranges.append(energy_range)
for dt, energy_range, change in zip(dt_values, energy_ranges, changes):
    print("dt =", dt, "energy_range =", energy_range, "change =", change)

for front_change, back_change in zip(changes[:-1], changes[1:]):
    assert front_change < back_change
print("테스트 통과")

x_005, y_005, vx_005, vy_005 = simulate(0.005, 1.5, 4001)
x_05, y_05, vx_05, vy_05 = simulate(0.05, 1.5, 401)
x_025, y_025, vx_025, vy_025 = simulate(0.025, 1.5, 801)
x_01, y_01, vx_01, vy_01 = simulate(0.01, 1.5, 2001)
x_0025, y_0025, vx_0025, vy_0025 = simulate(0.0025, 1.5, 8001)
x_00125, y_00125, vx_00125, vy_00125 = simulate(0.00125, 1.5, 16001)
x_000625, y_000625, vx_000625, vy_000625 = simulate(0.000625, 1.5, 32001)

position_reference = (x_00125[-1], y_00125[-1])
velocity_reference = (vx_00125[-1], vy_00125[-1])

position_difference_05 = np.sqrt((position_reference[0] - x_05[-1])**2 + (position_reference[1] - y_05[-1])**2)
print("position_difference_05 =", position_difference_05)
position_difference_025 = np.sqrt((x_025[-1] - position_reference[0])**2 + (y_025[-1] - position_reference[1])**2)
print("position_difference_025 =", position_difference_025)
position_difference_01 = np.sqrt((position_reference[0] - x_01[-1])**2 + (position_reference[1] - y_01[-1])**2)
print("position_difference_01 =", position_difference_01)
position_difference_0025 = np.sqrt((position_reference[0] - x_0025[-1])**2 + (position_reference[1] - y_0025[-1])**2)
print("position_difference_0025 =", position_difference_0025)
position_difference_000625 = np.sqrt((x_000625[-1] - position_reference[0])**2 + (y_000625[-1] - position_reference[1])**2)
print("position_difference_000625 =", position_difference_000625)
print()
velocity_difference_05 = np.sqrt((velocity_reference[0] - vx_05[-1])**2 + (velocity_reference[1] - vy_05[-1])**2)
print("velocity_difference_05 =", velocity_difference_05)
velocity_difference_025 = np.sqrt((vx_025[-1] - velocity_reference[0])**2 + (vy_025[-1] - velocity_reference[1])**2)
print("velocity_difference_025 =", velocity_difference_025)
velocity_difference_01 = np.sqrt((velocity_reference[0] - vx_01[-1])**2 + (velocity_reference[1] - vy_01[-1])**2)
print("velocity_difference_01 =", velocity_difference_01)
velocity_difference_0025 = np.sqrt((velocity_reference[0] - vx_0025[-1])**2 + (velocity_reference[1] - vy_0025[-1])**2)
print("velocity_difference_0025 =", velocity_difference_0025)
velocity_difference_000625 = np.sqrt((vx_000625[-1] - velocity_reference[0])**2 + (vy_000625[-1] - velocity_reference[1])**2)
print("velocity_difference_000625 =", velocity_difference_000625)
