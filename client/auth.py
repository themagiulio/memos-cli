from urllib.parse import urlparse
from client.session import session
from common.config import read_config, write_config


def signin(host, username, password):
    host = urlparse(host)
    host = host._replace(scheme='https')
    domain = host.path if host.path not in ('/', '') else host.netloc
    domain = domain.replace('/', '')
    url = host.scheme + '://' + domain + '/api/auth/signin'
    r = session.post(url, json={'username': username, 'password': password})

    if r.status_code == 200:
        user = r.json()['data']
        write_config('openId', user['openId'])
        write_config('host', host.scheme + '://' + domain)
        return user

    return None


def get_me():
    host = read_config('host')
    if host is None:
        return None

    r = session.get(host + '/api/user/me')
    if r.status_code == 200:
        return r.json()['data']

    return None
