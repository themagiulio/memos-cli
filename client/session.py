import requests
from common.config import read_config


def create_session():
    s = requests.Session()

    s.headers.update({
        'Content-Type': 'application/json'
    })

    open_id = read_config('openId')

    if open_id is not None:
        s.params['openId'] = open_id

    return s


session = create_session()
