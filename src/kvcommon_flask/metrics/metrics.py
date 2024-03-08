from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client import Histogram
from prometheus_client import Info
from prometheus_client import Summary


def incr_counter(metric: Counter | Gauge):
    from kvcommon_flask.vars import KVC_FLASK_METRICS_ENABLED

    if KVC_FLASK_METRICS_ENABLED:
        metric.inc()


def set_app_info(app_version: str):
    from kvcommon_flask.vars import KVC_FLASK_METRICS_ENABLED

    if KVC_FLASK_METRICS_ENABLED:
        APP_INFO.info(dict(version=app_version))


APP_INFO = Info("app", "Application info")


JOB_EVENT = Counter(
    "scheduled_job_event",
    "Gauge of scheduled job events by event enum",
    labelnames=[
        "job_id",
        "event",
    ],
)

# Total time spent from start to finish on a request
SECONDS_SERVER_REQUEST = Histogram(
    "seconds_server_request",
    "Time taken for server to handle request",
    labelnames=["path"],
)
