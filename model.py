def bmi(weigth: int, height_cm: int):
    height_m = height_cm/100
    return weigth/(height_m**2)