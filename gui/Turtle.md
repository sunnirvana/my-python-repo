
# Turtle
[Turtle库说明](https://docs.python.org/3.3/library/turtle.html#module-turtle)

## Rect


```python
from turtle import *

# 设置笔刷宽度
width(4)

forward(200)

right(90)

pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

done()
```

## Star


```python
from turtle import *

def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

for x in range(0, 250, 50):
    drawStar(x, 0)

done()

```

## Tree


```python
from turtle import *

# 设置色彩模式是RGB:
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

speed("fastest")

draw_tree(l, 4)

done()
```


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-1-eabc84a9fa89> in <module>()
         57 speed("fastest")
         58 
    ---> 59 draw_tree(l, 4)
         60 
         61 done()


    <ipython-input-1-eabc84a9fa89> in draw_tree(l, level)
         42 
         43     if level < lv:
    ---> 44         draw_tree(l, level + 1)
         45     bk(l)
         46     rt(2 * s)


    <ipython-input-1-eabc84a9fa89> in draw_tree(l, level)
         42 
         43     if level < lv:
    ---> 44         draw_tree(l, level + 1)
         45     bk(l)
         46     rt(2 * s)


    <ipython-input-1-eabc84a9fa89> in draw_tree(l, level)
         48 
         49     if level < lv:
    ---> 50         draw_tree(l, level + 1)
         51     bk(l)
         52     lt(s)


    <ipython-input-1-eabc84a9fa89> in draw_tree(l, level)
         48 
         49     if level < lv:
    ---> 50         draw_tree(l, level + 1)
         51     bk(l)
         52     lt(s)


    <ipython-input-1-eabc84a9fa89> in draw_tree(l, level)
         48 
         49     if level < lv:
    ---> 50         draw_tree(l, level + 1)
         51     bk(l)
         52     lt(s)


    <ipython-input-1-eabc84a9fa89> in draw_tree(l, level)
         48 
         49     if level < lv:
    ---> 50         draw_tree(l, level + 1)
         51     bk(l)
         52     lt(s)


    <ipython-input-1-eabc84a9fa89> in draw_tree(l, level)
         48 
         49     if level < lv:
    ---> 50         draw_tree(l, level + 1)
         51     bk(l)
         52     lt(s)


    <ipython-input-1-eabc84a9fa89> in draw_tree(l, level)
         42 
         43     if level < lv:
    ---> 44         draw_tree(l, level + 1)
         45     bk(l)
         46     rt(2 * s)


    <ipython-input-1-eabc84a9fa89> in draw_tree(l, level)
         42 
         43     if level < lv:
    ---> 44         draw_tree(l, level + 1)
         45     bk(l)
         46     rt(2 * s)


    <ipython-input-1-eabc84a9fa89> in draw_tree(l, level)
         48 
         49     if level < lv:
    ---> 50         draw_tree(l, level + 1)
         51     bk(l)
         52     lt(s)


    <ipython-input-1-eabc84a9fa89> in draw_tree(l, level)
         43     if level < lv:
         44         draw_tree(l, level + 1)
    ---> 45     bk(l)
         46     rt(2 * s)
         47     fd(l)


    /usr/local/anaconda3/lib/python3.7/turtle.py in bk(distance)


    /usr/local/anaconda3/lib/python3.7/turtle.py in back(self, distance)
       1655         (-30.00, 0.00)
       1656         """
    -> 1657         self._go(-distance)
       1658 
       1659     def right(self, angle):


    /usr/local/anaconda3/lib/python3.7/turtle.py in _go(self, distance)
       1603         """move turtle forward by specified distance"""
       1604         ende = self._position + self._orient * distance
    -> 1605         self._goto(ende)
       1606 
       1607     def _rotate(self, angle):


    /usr/local/anaconda3/lib/python3.7/turtle.py in _goto(self, end)
       3193                                        # of life, the universe and everything
       3194             self._newLine()
    -> 3195         self._update() #count=True)
       3196 
       3197     def _undogoto(self, entry):


    /usr/local/anaconda3/lib/python3.7/turtle.py in _update(self)
       2661             self._drawturtle()
       2662             screen._update()                  # TurtleScreenBase
    -> 2663             screen._delay(screen._delayvalue) # TurtleScreenBase
       2664         else:
       2665             self._update_data()


    /usr/local/anaconda3/lib/python3.7/turtle.py in _delay(self, delay)
        564     def _delay(self, delay):
        565         """Delay subsequent canvas actions for delay ms."""
    --> 566         self.cv.after(delay)
        567 
        568     def _iscolorstring(self, color):


    /usr/local/anaconda3/lib/python3.7/tkinter/__init__.py in after(self, ms, func, *args)
        739         if not func:
        740             # I'd rather use time.sleep(ms*0.001)
    --> 741             self.tk.call('after', ms)
        742             return None
        743         else:


    KeyboardInterrupt: 



```python
from turtle import *
from random import *
from math import *

def tree(n, l):
    pd()
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n/4)
    forward(l)
    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 + 0.6)
        right(b)
        tree(n-1,d)
        left(b+c)
        tree(n-1,d)
        right(c)
    else:
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n, n)
        circle(2)
        left(90)
    pu()
    backward(l)
    
bgcolor(0.5, 0.5, 0.5)
ht()
speed(0)
tracer(0, 0)
left(90)
pu()
backward(300)
tree(13,100)
done()

```
