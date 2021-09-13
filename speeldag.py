ToegangPrijs = 7.45
Personen = 4
PrijsGameSeat = 0.37
AantalVijfMinuten = 9
PrijsToegang = 43.12

print((ToegangPrijs * Personen) + (PrijsGameSeat * AantalVijfMinuten * Personen))
print('Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar '+ str(PrijsToegang) +' euro.')

print('vragenlijst')
AantalPersonen = int(input('Met hoeveel zijn jullie? '))
TijdVIPVR = int(input('Voor hoeveel minuten gaan jullie op de VIP VR gameseat? '))
PrijsToegang = (AantalPersonen * ToegangPrijs + TijdVIPVR + PrijsGameSeat)
print(str(PrijsToegang) + ' euro')