import numpy as np
import time
import json
import logging
import lib
from worker import app


logger = logging.getLogger(__name__)


@app.task(bind=True, name='average_of_random_walk')
def average_of_random_walk(self, s0, mu, sigma, days):
    return lib.average_of_random_walk(s0, mu, sigma, days)


@app.task(bind=True, name='average')
def average(self, numbers):
    return sum(numbers)/len(numbers)


@app.task(bind=True, name='add')
def add(self, a, b):
    return a + b