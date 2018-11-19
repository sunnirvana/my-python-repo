from io import BytesIO

f = BytesIO()
f.write(b'Hello')
f.write(b' ')
f.write(b'world')
print(f.getvalue())

data = '水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。'.encode('utf-8')
f = BytesIO(data)
print(f.readlines())
