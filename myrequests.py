import requests
import datetime


class Session:
    def __init__(self):
        super().__init__()
        self.s = requests.Session()

    def _get(self):
        pass

    def _post(self):
        pass


class RequestError(Exception):
    def __init__(self, status, message=None):
        self.status = status
        self.message = message

    def __str__(self):
        if self.message is None:
            return str(self.status)
        else:
            return "%s (%s)" % (self.status, self.message)


def get(url, params=None, session=None, log_folder='requests/', *args, **kwargs):
    if session:
        r = session.get(url)
    else:
        r = requests.get(url, params, *args)
    if not r or not r.ok:
        raise RequestError(r.reason, url)
    return r


def gete(url, params=None, session=None, *args, **kwargs):
    if session:
        r = session.get(url)
    else:
        r = requests.get(url, params, args)
    timestamp = datetime.now().strftime('%Y%m%d %H %M %S %f')[:-3]
    name = "requests/%s-get" % timestamp
    return r, name + ".html"


def poste(url, params, headers, session=None, *args, **kwargs):
    if session:
        r = session.post(url, params, headers)
    else:
        session = requests.Session()
        r = session.post(url, params, *args)
    return r, session