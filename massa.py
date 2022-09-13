rost = 2
ves = 120 
ksh = 1000
vrem_ak = 60

dl_sh = rost/4 + 0.37 #ì
rasst = dl_sh * ksh #ì
skorost = rasst/(vrem_ak)/60 #m/s

kalorii = 0.035 * ves + (skorost*skorost/rost) * 0.029 * ves #kk v min

print("rasst METR", rasst)
print( "KOLVO kalorii {0:.0f}".format(kalorii))
print("rasst KM {0:.0f}".format(rasst/1000))

if (rasst/1000) > 5:
    print("Well done")
else:
    print("Do your best")
