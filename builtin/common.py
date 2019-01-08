import os
import hashlib
import datetime
import getpass
import socket
import pathlib
from enum import Enum


def project_root_path():
    return str(pathlib.Path(os.path.abspath(__file__)).parent.parent)


def log_root_path():
    path = os.path.join(
        str(pathlib.Path(os.path.abspath(__file__)).parent.parent.parent), 'log')
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def get_file_md5(filename):
    return hashlib.md5(open(filename, 'rb').read()).hexdigest()


def get_string_md5(string):
    assert isinstance(string, str) or isinstance(string, bytes)

    _str = string if isinstance(string, bytes) else string.encode('utf-8')
    return hashlib.md5(_str).hexdigest()


def get_now_timestamp():
    return int(datetime.datetime.now().timestamp())


def get_login_user():
    return getpass.getuser()


def get_hostname():
    return socket.gethostname()


def detect_env():
    sharefs = pathlib.Path('/unsullied/sharefs')
    if sharefs.exists() and sharefs.is_dir():
        return 'brainpp'
    else:
        return 'local'

# if(sys.argv[2].lower() == 'md5'):
#             print(hashlib.md5(open(sys.argv[1], 'rb').read()).hexdigest())
#         elif(sys.argv[2].lower() == 'sha-1'):
#             print (hashlib.sha1(open(sys.argv[1],'rb').read()).hexdigest()  )
#         elif(sys.argv[2].lower() == 'sha-256'):
#             print (hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest()  )
#         elif(sys.argv[2].lower() == 'sha-512'):
#             print (hashlib.sha512(open(sys.argv[1],'rb').read()).hexdigest()  )
#         else:
#             print ('[-]Please input a correct encryption algorithm.'  )


if __name__ == "__main__":
    print(get_file_md5('common.py'))
    print(get_string_md5('abc'))
    print(get_string_md5(b'abc'))
    print(get_now_timestamp())
    print(get_login_user())
    print(get_hostname())
