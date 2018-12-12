
# ThreadLocal
一个`ThreadLocal`变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。`ThreadLocal`解决了参数在一个线程中各个函数之间互相传递的问题。
`ThreadLocal`最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。


```python
import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.currentThread().name))
    
def process_thread(name):
    local_school.student = name
    process_student()
    

t1 = threading.Thread(target=process_thread, args=('Alice', ), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob', ), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
    
```

    Hello, Alice (in Thread-A)
    Hello, Bob (in Thread-B)

