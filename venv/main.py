pytanie = True
pytanie2 = True

while pytanie:
    wyswietlenie = input("Czy chcesz wyswietlic liste? (Y/N):" )
    if wyswietlenie.lower() == 'y':
        print('OK wyswietlam liste')
        pytanie = False

        while pytanie2:
            wyswietlenie2 = input("Czy chcesz dodac osobe? (Y/N):")
            if wyswietlenie2.lower() == 'y':
                name = input("Podaj imie: ")
                print('dodac do listy, wygenerowac id oraz haslo')
                pytanie2 = False
            elif wyswietlenie2.lower() == 'n':
                print('ok, here is the list without adding and bye')
                break
            else:
                print('please input Y or N')
    elif wyswietlenie.lower() == "n":
        print('ok, closing app, bye')
        break
    else:
        print('please input Y or N')