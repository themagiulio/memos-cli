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


    def post(self, body={}):
        url = self.path.strip('/')
        r = session.post(url, json=body)
        if r.status_code == 200:
            return r.json()['data']
        return None


    def patch(self, item_id, body={}):
        url = urljoin(self.path, item_id).strip('/')
        r = session.patch(url, json=body)
        return r.status_code == 200


    def delete(self, item__id):
        url = urljoin(self.path, item__id).strip('/')
        r = session.delete(url)
        return r.status_code == 200
