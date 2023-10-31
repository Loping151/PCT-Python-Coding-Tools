import signal, sys


def handler(*_):
    print('Caught SIGTSTP, exiting...')
    sys.exit(0)
signal.signal(signal.SIGTSTP, handler)

def cuda_free_always(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print('Caught KeyboardInterrupt, exiting...')
            sys.exit(0)
    return wrapper
