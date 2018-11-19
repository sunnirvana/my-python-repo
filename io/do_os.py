import time
import os
from shutil import copyfile

print(os.uname())
print(os.environ)
print(os.name)
print(os.environ.get('PATH'))

print(os.path.abspath('.'))
print(os.path.join('.', 'test'))
print(os.path.split('/Users/michael/testdir/file.txt'))
print(os.path.splitext('/Users/michael/testdir/file.txt'))

with open('./test_io', 'w') as f:
    f.write(' ')
time.sleep(5)
os.rename('test_io', 'renamed_test_io')
time.sleep(5)
os.remove('renamed_test_io')


root = './hello'
os.mkdir(root)
os.rmdir(root)

leaves = './hello/world/to/my/friends'
os.makedirs(leaves)
print(os.listdir(root))
os.removedirs(leaves)
