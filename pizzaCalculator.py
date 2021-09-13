# Bilal Achrifi Pizza Calculator
small = 6.99
medium = 11.99
large = 16.99
# Hierboven zijn de assignments.
print("U kunt kiezen uit small, medium en large pizza's")
print('De kosten zijn: small - 6,99€, medium - 11,99€, large - 16,99€')
PizzaGrootte = int(input("Hoeveel small-pizza's wilt u? "))
PizzaGrootte2 = int(input("Hoeveel medium-pizza's wilt u? "))
PizzaGrootte3 = int(input("Hoeveel large-pizza's wilt u? "))
# De vragen hierboven worden aan de klant gesteld.
print('----------------------------------------------')
print('|  Aantal  small-pizza\'s      :   '+ str(PizzaGrootte) +'  ')
print('|  Aantal  medium-pizza\'s     :   '+ str(PizzaGrootte2) +'  ')
print('|  Aantal  large-pizza\'s      :   '+ str(PizzaGrootte3) +'  ')
print('|  Bedrag                     :   €'+ str(PizzaGrootte * small + PizzaGrootte2 * medium + PizzaGrootte3 * large) +'           ')
print('----------------------------------------------')
# Hierboven wordt het totaalbedrag berekend en weergegeven voor de klant


