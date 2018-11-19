from datetime import datetime

with open('date', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('date', 'r') as f:
    print('read as normal file: {}'.format(f.read()))

with open('date', 'rb') as f:
    print('read as binary format: {}'.format(f.read()))
