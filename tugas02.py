J = int(input("masukan jari jari: "))
T = int(input("masukan tinggi: "))
la = int(input("luas alas: "))
ka = int(input("masukan keliling alas: "))

phi = 22/7

luas = (2*la)+(ka*T)
volume = (phi*J*J*J*T)

print("luas tabung adalah: ", luas)
print("volume tabung adalah: ", volume)