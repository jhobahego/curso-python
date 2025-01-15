# Pidiendo datos desde terminal
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuál es tu edad? ')

print('tipo de la edad', type(age))
age = int(age)

print('Tu nombre es', name, 'y tienes', age, 'años')

print('tipo de la edad corregido:', type(age))

print("Obteniendo multiples valores a la vez")
pais, ciudad = input('Ingresa tu país y ciudad separados por coma: ').split(',')

print('Tu país es', pais, 'y tu ciudad es', ciudad)