def liida(number_1, number_2):
    vastus = number_1 + number_2
    return vastus

def lahuta(number_1, number_2):
    vastus = number_1 - number_2
    return vastus

def kalkulaator(number_1, number_2, operatsioon):
    if operatsioon == "+":
        return liida(number_1, number_2)
    if operatsioon == "-":
        return lahuta(number_1, number_2)
    print("EI OSKA")

a = 5
b = 6
tulemus = liida(a, b)
print(tulemus)
