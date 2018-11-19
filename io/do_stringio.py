from io import StringIO

f = StringIO()
f.write('Hello')
f.write(' ')
f.write('world')
print(f.getvalue())

f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break

    print(s.strip())
