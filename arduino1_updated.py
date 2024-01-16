from pyfirmata import Arduino


board = Arduino('COM5')
print(board.get_firmata_version)