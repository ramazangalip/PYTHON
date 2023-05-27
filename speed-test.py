import time

def dec_speed_test(count):
    def  speed_test(fn):
        def wrapper(*args,**kwargs):
            start_time = time.perf_counter()
            print(f"{fn.__name__} metodu çalışıyor...")
            for _ in range(count):
             result = fn(*args,**kwargs)
             end_time = time.perf_counter()
             run_time = end_time - start_time
             print(f" geçen süre:{run_time}")
             return  result
        return wrapper
    return speed_test

@dec_speed_test(count=2)
def sum_gen():
    return sum((x for x in range(1000)))

@dec_speed_test(count=3)
def sum_list():
    return sum([x for x in range(1000)])  

print(sum_gen())
print(sum_list())