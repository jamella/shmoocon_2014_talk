import logging
import os
from workers import MasscanWorker

log = logging.getLogger(__name__)

def run(WorkerClass):
    def wrapped():
        worker = WorkerClass()
        log.info('Started worker:%s:%s', worker.__class__.__name__, os.getpid())
        for job in worker:
            if job:
                logger.debug('Completed job: %s', str(job)[:50])
    return wrapped

# host_regex, func, count
workers = [
    {'host': 'computer',
     'func': run(MasscanWorker),
     'count': 10,
     },
    {'host': 's2',
     'func': run(MasscanWorker),
     'count': 1,
     },
    ]