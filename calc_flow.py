import numpy as np
from utils.read_input_file import p_air, dens_air, h_ratio
from utils.calc_coefficient import comp_condensation_coef
from utils.calc_density import calc_density


def forward_flow(c_c, A, p_up, dens_up) -> '押出流量':
    h_ratio_rev = 1 / h_ratio
    return (dens_up / dens_air) * (c_c * A * ((p_up / p_air) ** (-1 * h_ratio_rev)) * (((2 / (1 - h_ratio_rev)) * (p_up / dens_up) * (1 - (p_up / p_air) ** (h_ratio_rev - 1))) ** (1 / 2)))


def back_flow(c_c, A, p_down) -> '吸込流量':
    h_ratio_rev = 1 / h_ratio
    return c_c * A * ((p_air / p_down) ** (-1 * h_ratio_rev)) * (((2 / (1 - h_ratio_rev)) * (p_air / dens_air) * (1 - (p_air / p_down) ** (h_ratio_rev - 1))) ** (1 / 2))


def calc_flow_and_mass_flow(f_ci, p_list, A):
    flow_list = []
    mass_flow_list = []
    dens_list = []
    for p in p_list:
        dens = calc_density(p)
        if (p > p_air):
            c_c = comp_condensation_coef(f_ci, p, p_air)
            flow = forward_flow(c_c, A, p, dens)
        else:
            c_c = comp_condensation_coef(f_ci, p_air, p)
            flow = (-1) * back_flow(c_c, A, p)
        dens_list.append(dens)
        flow_list.append(flow)
        mass_flow_list.append(dens*flow)
    return flow_list, mass_flow_list, dens_list
