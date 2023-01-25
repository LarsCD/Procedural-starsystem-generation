import datetime, time

for i in range(100000000000000000000):
    print(f'{i}:   {datetime.datetime.now()}')
    time.sleep(0.01)