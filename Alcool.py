print("Questo programma ti consente di calcolare la % di alcool nella tua bibita")
quantita = float(input("scrivi quanti ml è la tua bevanda:"))
gradi = float(input("scrivi qual'è la gradazione alcolica della bevanda senza il simbolo % :"))
scelta = float(input("scrivi '1' per continuare o '2' per uscire:"))
result = (quantita*gradi/100)*0.79

if scelta == 1:
	 
  print(result, "gr")
  sesso = str(input("inserisci il tuo sesso con 'f' o 'm'"))
  age = int(input("inserisci la tua età"))
else:
	raise Exception
		
if int(input("scrivi 1 per sapere se hai assunto una corretta\n quantità di alcool, 2 per uscire")) == 1:
	print("stiamo calcolando... ")
	
if (sesso == "m" and result<= 35 and age >= 16) or (sesso=="f" and result <= 24 and age >=18):
    if sesso == "m":
	    print("i tuoi valori sono stabili, hai assunto",result,"su 35gr")
	    
    else:
	    print("i tuoi valori sono stabili, hai assunto",result,"su 24gr")
	    
else:
    print("i tuoi valori non sono stabili!!!")
