import logging
import typing as t


from flask_http_middleware import BaseHTTPMiddleware

from kvcommon.urls import urlparse_ignore_scheme
from kvcommon_flask import metrics
from kvcommon_flask.context import set_flask_context_local
from kvcommon import logger

LOG = logger.get_logger("kvc-flask")


def is_meta_url(url: str, prefix: str | None = None) -> bool:
    if (prefix and url.startswith(prefix)) or url.startswith("/healthz/"):
        return True
    return False


class KVCFlaskMiddleware(BaseHTTPMiddleware):
    _meta_prefix: str

    def __init__(self, meta_prefix: str | None):
        if meta_prefix:
            self._meta_prefix = meta_prefix
        super().__init__()

    def dispatch(self, request, call_next):
        with metrics.SECONDS_SERVER_REQUEST.labels().time():
            url_parts = urlparse_ignore_scheme(request.url, request.scheme)
            url_path: str = url_parts.path
            set_flask_context_local("url_parts", url_parts)

            is_meta: bool = is_meta_url(url_path, prefix=self._meta_prefix)
            set_flask_context_local("is_meta_request", is_meta)

            response = call_next(request)

        return response
