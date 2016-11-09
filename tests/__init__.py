from tw2.core import core, middleware

_request_local = {}
_request_id = 'id'


def request_local_tst():
    global _request_local, _request_id
    if _request_local is None:
        _request_local = {}
    if _request_id not in _request_local:
        _request_local[_request_id] = {}
    return _request_local[_request_id]


def setup():
    core.request_local = request_local_tst
    core.request_local().setdefault('middleware',
                                    middleware.make_middleware())
