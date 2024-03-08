import pytest

# Import all packages/modules to expose ImportErrors and the like
from kvcommon_flask import metrics
from kvcommon_flask import traces
from kvcommon_flask import context
from kvcommon_flask import middleware
from kvcommon_flask import scheduler
from kvcommon_flask import vars


# Null test to make pytest happy for now
def test_null():
    assert metrics is not None
    assert traces is not None
    assert context is not None
    assert middleware is not None
    assert scheduler is not None
    assert vars is not None
