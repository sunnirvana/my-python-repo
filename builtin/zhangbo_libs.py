import base64
import os
from functools import wraps
import zerorpc
import importlib


def bin2b64c(fpath):
    try:
        fname = os.path.basename(fpath)
        head = bytes(fname + '@', encoding='utf-8')
        with open(fpath, 'rb') as file:
            b64str = base64.b64encode(file.read())
        return head + b64str
    except Exception as e:
        raise (e)


def b66c2bin(b64code, fpath=''):
    try:
        fname = str(b64code).split('@')[0].split(
            "'")[-1] if os.path.basename(fpath) == '' else os.path.basename(fpath)
        ori_data = bytes(str(b64code).split('@')[-1], encoding='utf-8')
        data = base64.b64decode(ori_data)
        with open(os.path.join(os.path.dirname(fpath), fname), 'wb') as file:
            file.write(data)
    except Exception as e:
        raise (e)


def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


# @singleton
class rpc(object):
    _methods = {}

    def __init__(self, cls):
        self._cls = cls
        obj = self._cls()
        prefix = self._cls.__name__
        self._methods.update(
            {'{}:{}'.format(prefix, k): getattr(obj, k) for k in dir(
                obj) if not k.startswith('_') and callable(getattr(obj, k))}
        )

    @classmethod
    def methods(cls):
        return cls._methods


class Server(object):
    def __init__(self, **kwargs):
        self._methods = kwargs.get('methods', None)
        self._ip = kwargs.get('ip', '0.0.0.0')
        self._port = kwargs.get('port', '4321')
        self._heartbeat = kwargs.get('heartbeat', 5)

        if self._methods is None:
            raise RuntimeError('缺少必要参数: methods')

    def start(self):
        server = zerorpc.Server(self._methods)
        server.bind("tcp://{}:{}".format(self._ip, self._port))
        print("server start \ntcp://{}:{}".format(self._ip, self._port))
        server.run()


class Client(zerorpc.Client):
    def __init__(self, *args, **kwargs):
        self._prefix = kwargs.pop("prefix", "")
        super(Client, self).__init__(*args, **kwargs)

    def set_prefix(self, prefix):
        self._prefix = prefix

    def __getattr__(self, method):
        method = ":".join([self._prefix, method]) if self._prefix else method
        return lambda *args, **kwargs: self(method, *args, **kwargs)
