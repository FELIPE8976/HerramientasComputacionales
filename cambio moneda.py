cop = eval(input("Ingrese el valor a cambiar en pesos colombianos: "))
usd = cop * 0.00028
yen = cop * 0.030
euro = cop * 0.00023
t1 =  usd - (usd * 0.02) 
t2 = yen - (yen * 0.02) 
t3 = euro - (euro * 0.02)
lista = [t1,t2,t3]
print("El valor que se le entregara en usd, yen o euro es respectivamente: "  + str(lista))