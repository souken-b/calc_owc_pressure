import yaml
import numpy as np

global p_air, dens_air, h_ratio
# 大気圧
p_air = 101325
# 空気密度
dens_air = 1.225
# 比熱比
h_ratio = 1.4


def read_input_value(load_path):
    try:
        with open(load_path, 'r') as yml:
            input_data = yaml.safe_load(yml)
    except Exception as e:
        print(e)
    return input_data


def init_input_data(input_data):
    global p_air, dens_air, h_ratio
    period = input_data['input']['period']
    n = input_data['input']['n']
    n_ratio = input_data['input']['n_ratio']
    D0 = input_data['input']['D0']
    Zd = input_data['input']['Zd']
    Zd0 = input_data['input']['Zd0']
    phase_diff = input_data['input']['phase_diff']
    p0 = input_data['input']['p0']
    p0_delta = input_data['input']['p0_delta']
    # 15周期分
    total_time = period * 15
    # 絞り直径比
    d_ratio = n_ratio ** (1/2)
    n_diam = D0 * d_ratio
    # カラム内断面積
    A0 = ((D0 / 2) ** 2) * np.pi
    A = A0 * (d_ratio ** 2)
    return period, n, total_time, n_diam, D0, Zd, Zd0, phase_diff, p0, p0_delta, d_ratio, A, A0
