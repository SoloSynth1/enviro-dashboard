from environs import Env

env = Env()
env.read_env()

SQLITE_DB = env('SQLITE_DB')
