from bleach import clean


def sanitize(request_data):
    return {k: clean(v) if not isinstance(v, bool) else v for k, v in request_data.items()}
