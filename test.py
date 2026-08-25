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