import os
import sys
import logging
from celery import Celery
from celery.signals import after_setup_logger


app = Celery(__name__)
app.conf.update({
    'broker_url': os.environ['CELERY_BROKER_URL'],
    'imports': ('tasks',),
    'result_backend': os.environ['CELERY_RESULT_BACKEND']})


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    sh = logging.StreamHandler(sys.stdout)
    logger.addHandler(sh)
