import concurrent.futures
from time import sleep, perf_counter


secs = input("Seconds to sleep function separated by ';' : ")
secs = secs.split(";")
secs = map(lambda x: int(x), secs)

start = perf_counter()

def sleep_around(sec):
    """
    Sleep for given seconds
    """
    print(f"Sleeping for {sec} second(s)")
    sleep(sec)
    return f"Done sleeping...{sec}"

# Create and execute thread with ThreadPoolExecutor 
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [executor.submit(sleep_around, sec) for sec in secs]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())


# Using the map method
with concurrent.futures.ThreadPoolExecutor() as mapper:
    print("\n\nMapping threads")
    results = mapper.map(sleep_around, secs)

    for result in results:
        print(result)

finish = perf_counter()
print(f"Done execunting in {round(finish-start, 2)} seconds")