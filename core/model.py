import math

def pressure(shots_on_target, shots, corners, dangerous_attacks, xg):
    return (
        22*shots_on_target +
        5*shots +
        6*corners +
        0.15*dangerous_attacks +
        10*xg
    )

def probability(pressure_score, minute):
    if minute < 20:
        time_weight = 0.7
    elif minute < 55:
        time_weight = 1.0
    elif minute < 75:
        time_weight = 1.2
    else:
        time_weight = 1.35

    raw = pressure_score * time_weight / 100
    return round(100*(1/(1+math.exp(-raw))),1)