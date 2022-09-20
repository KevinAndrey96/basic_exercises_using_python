def girar(orientacion_actual, sentido):
    if orientacion_actual == 'N':
        if sentido == 'R':
            return 'E'
        if sentido == 'L':
            return 'W'
        if sentido == '.':
            return orientacion_actual
        if sentido == 'H':
            return 'S'
    if orientacion_actual == 'E':
        if sentido == 'R':
            return 'S'
        if sentido == 'L':
            return 'N'
        if sentido == '.':
            return orientacion_actual
        if sentido == 'H':
            return 'W'
    if orientacion_actual == 'S':
        if sentido == 'R':
            return 'W'
        if sentido == 'L':
            return 'E'
        if sentido == '.':
            return orientacion_actual
        if sentido == 'H':
            return 'N'
    if orientacion_actual == 'W':
        if sentido == 'R':
            return 'N'
        if sentido == 'L':
            return 'S'
        if sentido == '.':
            return orientacion_actual
        if sentido == 'H':
            return 'E'


def movimiento_robot(orientacion_actual, giro_1, giro_2, giro_3):
    return girar(girar(girar(orientacion_actual, giro_1), giro_2), giro_3)


if __name__ == '__main__':
    print(movimiento_robot('N', 'R', 'H', '.'))
