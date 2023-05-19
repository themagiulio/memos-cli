from urllib.parse import urljoin
from client.session import session


class Model:
    path = None

    def __init__(self):
        host = 'https://memos.giuliodematte.is/api/'
        self.path = urljoin(host, self.path)


    def get(self, item_id):
        url = urljoin(self.path, item_id).strip('/')
        r = session.get(url)
        if r.status_code == 200:
            return r.json()['data']
        return None


    def post(self):
        pass


    def patch(self):
        pass


    def delete(self):
        pass
