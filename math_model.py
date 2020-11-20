# -*- coding: utf-8 -*-
"""
Created on Nov 5th 10:38 pm 2020

@author: Alessandro Snyder

Based on David Wang's original command-line implementation in math_model.py
This version breaks the graph generation into functions for model_UI.py to use
"""
import numpy as np

C = 1.520
u = 0.117
g = 1.966


def get_plot_data(yo, is_od600):
    """
    yo: The initial y value of the plot in either cells/mL or OD600
    is_od600: A boolean tracking the units of yo
    """
    if not is_od600:
        yo = (yo * 10 ** 6) / 1E8

    t = np.array(range(100))
    y = yo + C / (1 + np.exp((4 * u / C) * (g - t) + 2))

    if not is_od600:
        y = y * 1E8

    return t, y


def get_peak(y):
    j = y[0]
    peak = 0
    for i in y[1:-1]:
        if (i - j) / j > 0.01:
            j = i
        else:
            peak = j
            break

    return peak/1E8



