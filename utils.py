def input_float(mensaje):
    try:
        return float(input(mensaje))
    except ValueError:
        return None


def input_int(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        return None
