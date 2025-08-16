from datetime import timedelta

default_args = {
    "depens_on_past": False,
    "catchup": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "owner": "localhost"
}

tz_jakarta = "Asia/Jakarta"