# Ejemplo de decorators del video de Corey Schafer
# En el minuto 17:50
# función que sirve para saber cuantas veces es ejecutada una función

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {}'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time

@my_timer
def display_info(name, age):
    time.sleep(1.3)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Hank', 30)