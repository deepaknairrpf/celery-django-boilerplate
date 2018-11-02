from celery.task import periodic_task
from datetime import timedelta

@periodic_task(run_every=timedelta(seconds=30))
def hello():
    print("Hello there!")