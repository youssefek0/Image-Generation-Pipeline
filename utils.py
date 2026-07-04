from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential_jitter,
    retry_if_exception_type,
)

import requests


@retry(
    stop=stop_after_attempt(4),
    wait=wait_exponential_jitter(initial=1, max=8),
    retry=retry_if_exception_type(
        (
            requests.exceptions.ConnectTimeout,
            requests.exceptions.ReadTimeout,
        )
    ),
)
def retry_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)