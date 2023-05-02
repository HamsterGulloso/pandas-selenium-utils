def month_to_int(text):
    month_ini = text[:3].lower()
    if month_ini == "jan":
        return 1
    if month_ini == "fev":
        return 2
    if month_ini == "mar":
        return 3
    if month_ini == "abr":
        return 4
    if month_ini == "mai":
        return 5
    if month_ini == "jun":
        return 6
    if month_ini == "jul":
        return 7
    if month_ini == "ago":
        return 8
    if month_ini == "set":
        return 9
    if month_ini == "out":
        return 10
    if month_ini == "nov":
        return 11
    if month_ini == "dez":
        return 12
    raise ValueError()