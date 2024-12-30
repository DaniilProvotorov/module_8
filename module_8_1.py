def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError as exc:
        a_new = str(a)
        b_new = str(b)
        print(a_new + b_new)
    else: print('Мы справились!')
    finally: print('В любом случае, мы возьмем свое!')

add_everything_up(6, 'error')