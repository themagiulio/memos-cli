from urllib.parse import urljoin
from client.session import session
from common.config import read_config


class Model:
    path = None

    def __init__(self):
        host = read_config('host')
        host = urljoin(host, 'api/')
        self.path = urljoin(host, self.path)


    def get(self, item_id, params={}):
        url = urljoin(self.path, item_id).strip('/')
        r = session.get(url, params=params)
        if r.status_code == 200:
            return r.json()['data']
        return None


    def post(self):
        pass


    def patch(self, item_id, body={}):
        url = urljoin(self.path, item_id).strip('/')
        r = session.patch(url, json=body)
        if r.status_code == 200:
            return True
        return False


    def delete(self):
        pass
