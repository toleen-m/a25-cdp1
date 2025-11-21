nombre = -21
print(nombre)

nombre2 = int(-6)
print(nombre2)

nombre3 = int(True)
print(nombre3)

nombre4 = int('22', 16)
print(nombre4)

# 22 -> sur une base de 16
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f
# 22 = 2 x(0*16)puissance 0 + 2x(1*16) puissance 1 = 2 + 32 = 34. 
# 22 = 2 x(0*10)puissance 0 + 2 (1*10) puissance 1 
# 22 =  2 x (0x8)puissance 1 + 2 (1x8) puissance 1

print(int('11', 2))

print(int('0X22', 0))
print(int('0O22', 0))
print(int('0b11', 0))
print(int('0b111', 0))