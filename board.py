from coral.enviro.board import EnviroBoard

board = EnviroBoard()

def get_temperature():
    return board.temperature

def get_humidity():
    return board.humidity

def get_ambient_light():
    return board.ambient_light

def get_pressure():
    return board.pressure
