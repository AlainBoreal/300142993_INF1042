def is_number(valeur):
    try:
        float(valeur)
        return True
    except ValueError:
        return False

def is_float(valeur):
    return is_number(valeur) and '.' in valeur

def is_positive_number(valeur):
    return is_number(valeur) and float(valeur) > 0
