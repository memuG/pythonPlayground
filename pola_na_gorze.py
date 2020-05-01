def pole_prostokata(a, b):
    return a * b


def pole_trojkata(a, b):
    return (a * b) / 2


def wymus_float(nazwa_zmiennej):
    while True:
        try:
            zmienna = float(input("{nazwa}: ".format(nazwa=nazwa_zmiennej)))
        except ValueError:
            print('Podaj liczbę!')
        else:
            return zmienna


szerokosc = wymus_float("szerokosc")  # 2.500
wysokosc = wymus_float("wysokosc")  # 2.450
szerokosc_do_skosu = wymus_float("szerokosc_do_skosu")  # 1.200
skos = wymus_float("skos")  # 1.400
wysokosc_do_skosu = wymus_float("wysokosc_do_skosu")  # 1.950
glebokosc = wymus_float("glebokosc")  # 3.400
szerokosc_od_skosu = wymus_float("szerokosc_od_skosu")  # 1.300
wysokosc_skosu = wymus_float("wysokosc_skosu")  # 0.500

wyzsza_sciana = pole_prostokata(wysokosc, glebokosc)
sufit_poziomy = pole_prostokata(szerokosc_do_skosu, glebokosc)
trzecie_pole = pole_prostokata(wysokosc, szerokosc_do_skosu)
czwarte_pole = pole_prostokata(szerokosc_od_skosu, wysokosc_do_skosu)
piate_pole = pole_trojkata(wysokosc_skosu, szerokosc_od_skosu)
sufit_skos = pole_prostokata(skos, glebokosc)
nizsza_sciana = pole_prostokata(wysokosc_do_skosu, glebokosc)

sciany_trapez = sum([trzecie_pole, piate_pole, czwarte_pole]) * 2
suma = sum([wyzsza_sciana, sufit_poziomy, sciany_trapez, sufit_skos, nizsza_sciana])

print("\n================================================\n")
print("Ściany trapez : " + format(sciany_trapez, '.2f'))

print("Wyższa ściana : " + format(wyzsza_sciana, '.2f'))
print("Sufit poziomy : " + format(sufit_poziomy, '.2f'))
print("Sufit Skos : " + format(sufit_skos, '.2f'))
print("Niższa ściana : " + format(nizsza_sciana, '.2f'))
print("----------------------------------------------------")
print("Suma : " + format(suma, '.2f'))
print("----------------------------------------------------")
wysokosc_plyty = wymus_float("wysokosc_plyty")
szerokosc_plyty = wymus_float("szerokosc_plyty")
powierzchnia_plyty = wysokosc_plyty * szerokosc_plyty
print("Powierzchnia płyty : " + format(powierzchnia_plyty, '.2f'))
print("Ilość płyt: " + format(suma / powierzchnia_plyty, '.2f'))
