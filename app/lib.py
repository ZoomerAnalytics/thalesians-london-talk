import numpy as np


def random_walk(s0, mu, sigma, days):
    dt = 1/365.
    prices = np.zeros(days)
    shocks = np.zeros(days)
    prices[0] = s0
    for i in range(1, days):
        e = np.random.normal(loc=mu * dt, scale=sigma * np.sqrt(dt))
        prices[i] = prices[i-1] * (1 + e)
    return prices


def average_of_random_walk(s0, mu, sigma, days):
    return np.average(random_walk(s0, mu, sigma, days))
