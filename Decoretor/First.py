import time

def timer(func):
    def wraper(*args , **kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} ran is {end-start}")
        return result
    return wraper

@timer
def timetaking (n):
    time.sleep(n)

print(timetaking(4))