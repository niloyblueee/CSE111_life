def hospital_fee(**details):
    max_cash=0
    max_giver=''
    for giver in details.keys():
        if details[giver]>max_cash:
            max_cash=details[giver]
            max_giver=giver
        elif details[giver]==max_cash:
            max_giver+=','+giver    
    print(f'Highest fee was {max_cash} tk which was paid by {max_giver}.')
    return max_cash,max_giver


max_amount, max_payer = hospital_fee(Neymar =1000, Dembele = 600, Reus = 500, Bale = 1000)
max_amount, max_payer = hospital_fee(Mashrafe =400, Bumrah = 900, Steyn = 1200, Cummins = 900, Wood = 400, Marsh = 700)
