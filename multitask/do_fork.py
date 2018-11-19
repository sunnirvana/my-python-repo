import os

print('Process (%s) start...' % os.getpid())
# fork only works on Linux/Mac/Unix
pid = os.fork()

if pid == 0:
    # pid == 0 ==> in child process
    print('i am child process (%d), and my parent process is %d' %
          (os.getpid(), os.getppid()))
else:
    # pid != 0 ==> in parent process, and pid is the child process
    print('i just created child process (%s), my pid is %s' % (pid, os.getpid()))
