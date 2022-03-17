tekst ="Twórca Emmy, start-up o nazwie Stealth, nazywa ją „niezależną sztuczną inteligencją” zaprojektowaną, by świadczyć profesjonalne usługi, takie jak badania i analiza. Odkąd w modzie są prognozy, że sztuczna inteligencja (ang artificial intelligence, AI) zastąpi pracowników biurowych, w tym również dziennikarzy, chciałam to sprawdzić na własnej skórze.\n\n\n Emma rzeczywiście była szybka – dane wysłała w 12 minut. Mi zajęło to 35. Jej wersja była też lepsza, niż się spodziewałam. Fakty się zgadzały, zawarła nawet trafne treści, takie jak możliwość Brexitu (choć podzielała wątpliwą opinię, że wyjście z Unii Europejskiej byłoby niezwykle korzystne dla brytyjskiej gospodarki). \n\n\n Ale ku mojej uldze zabrakło jej najważniejszej umiejętności dziennikarza – zdolności do oddzielania interesujących informacji od tych zwyczajnie nudnych. Choć prawidłowo podkreśliła, że stopa bezrobocia się nie zmieniła, Emma nie zauważyła, że liczba osób szukających zatrudnienia wzrosła po raz pierwszy od prawie roku."
if("Emma" in tekst):
  print("Liczba powtorzen slowa Emma w tekscie to:", tekst.count("Emma"))
else:
  print("Slowo Emma nie wystepuje w tekscie.")
print("\n Zamieniony tekst na same duze litery:\n")
print(tekst.upper())
kopia = tekst.split(' ')
lista = kopia[::3]
print("\nLista wyrazow z tekstu:\n")
print(lista)
print("\nLiczba zdan w tekscie wynosi:\n")
print(tekst.count("."))
