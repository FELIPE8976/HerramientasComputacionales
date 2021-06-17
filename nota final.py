parcial1 = eval(input("Ingrese la nota de su primer parcial: "))
parcial2 = eval(input("Ingrese la nota de su segundo parcial: "))
taller = eval(input("Ingrese la nota del taller: "))
proyecto = eval(input("Ingrese la nota de su proyecto: "))
np1 = parcial1 * 0.25
np2 = parcial2 * 0.25
nt = taller * 0.20
npr = proyecto * 0.30
nf = (np1 + np2 + nt + npr) 
print("Su nota final es: " + str(nf))
