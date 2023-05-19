from http.cookiejar import CookieJar
import requests
from common.config import read_config


def create_session():
    s = requests.Session()

    s.headers.update({
        'Content-Type': 'application/json'
    })

    access_token = read_config('access-token')
    refresh_token = read_config('refresh-token')

    if access_token is not None and refresh_token is not None:
        cookies = requests.utils.cookiejar_from_dict({
            'access-token': access_token,
            'refresh-token': refresh_token,
            '_csrf': ''
        })
        s.cookies.update(cookies)

    return s


session = create_session()
