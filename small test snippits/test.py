from alive_progress import alive_bar; import time


def compute():
    for i in range(1000):
        time.sleep(0.02)
        yield  # insert this :)


with alive_bar(1000) as bar:
    for i in compute():
        bar()

print('hi')