from varasto import Varasto


def main():
    mehua, olutta = luo_varastos()

    olutvarasto_tarkastus3(olutta)

    mehuvarasto_tarkastus3(mehua)

    varasto2()

    varasto()

    olutvarasto_tarkastus2(olutta)

    mehuvarasto_tarkastus2(mehua)

    olutvarasto_tarkastus1(olutta)

    mehovarasto_tarkastus1(mehua)


def luo_varastos():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")
    return mehua, olutta


def olutvarasto_tarkastus3(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def mehuvarasto_tarkastus3(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def varasto2():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)


def varasto():
    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def olutvarasto_tarkastus2(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")


def mehuvarasto_tarkastus2(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")


def olutvarasto_tarkastus1(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")


def mehovarasto_tarkastus1(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def asd():
    # tämä on pitkä rivi aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    moi = 1 + 1
    moi2 = moi + moi

    if moi + 5 < moi2:
        print("Kalaa")
        print("Kalaa")


if __name__ == "__main__":
    main()
    asd()
