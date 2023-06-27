import os


def get_env():
    try:
        return  os.environ['SYS_ENV']
    except KeyError:
        return 'SYS_ENV environment variable not set'

