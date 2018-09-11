import inspect

def add(x, y:int = 7, *args, z, t = 10, **kwargs) -> int:
    return x + y

for i in dir(inspect):
    print(i)

# sig = inspect.signature(add)
# print(sig)
#
# params = sig.parameters
# print(params)
#
# print(params['x'].annotation)
# print(params['y'].annotation)
# print(params['args'].annotation)
# print(params['z'].annotation)
# print(params['t'].annotation)
# print(params['kwargs'].annotation)
