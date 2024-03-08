from prometheus_client import start_http_server

from kvcommon_flask.vars import KVC_FLASK_METRICS_ENABLED as ENABLED
from kvcommon_flask.vars import KVC_FLASK_METRICS_PORT
from .metrics import JOB_EVENT

from .metrics import SECONDS_SERVER_REQUEST
from .metrics import incr_counter


def init_metrics():
    if ENABLED:
        start_http_server(KVC_FLASK_METRICS_PORT)

__all__ = [
    "ENABLED",
    "incr_counter",
    "init_metrics",
    "JOB_EVENT",
    "SECONDS_SERVER_REQUEST",
]
