def timer(func):
    import time

    def mesure(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()

        diff = t2 - t1
        print(f'{func.__name__} took {diff}s to execute')

        return result

    return mesure
