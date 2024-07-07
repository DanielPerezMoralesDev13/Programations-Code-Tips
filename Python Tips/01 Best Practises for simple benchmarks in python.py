# optimising code in python

# version 3.9 python

import time

start_time: float = time.perf_counter()
...
end_time: float = time.perf_counter()
print("total:", end_time - start_time)
def primerEjemplo() -> None:
    import gc
    from timeit import repeat, timeit
    gc.disable()
    list_comp: str = """my_list: list[int] = [i for i in range(10)]"""
    for_loop: str = """
    my_list: list[int] = []
    for i in range(10):
        my_list.append(i)
    """

    list_comp_time: float = min(repeat(list_comp, repeat=5,number=1_000_000))
    for_comp_time: float = min(repeat(for_loop, repeat=5,number=1_000_000))

    # list_comp_time: float = timeit(list_comp, number=1_000_000)
    # for_comp_time: float = timeit(for_loop, number=1_000_000)

    print(f"list comp: {list_comp_time:.3f}s")
    print(f"for loop: {for_comp_time:.3f}s")
