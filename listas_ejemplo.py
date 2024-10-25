nombres=[]#declarar lista vacia
nombres = ["Wacoldo", "Diogenes", "Wenceslao", "Amargo"]#lista con datos

'''#regresa 2 nombres
for i in range(2):
    nombre=input("Ingrese nombre: ")
    lista.append(nombre)'''#agrega nombres hasta 2 de acuerdo al anterior

print("Datos Registrados: ")
print(nombres)

for nombre in nombres:
    print(nombre)

buscado = input("Ingrese nombre a buscar: ")
#buscar en la lista
if buscado in nombres:
    print("Encontrado")
else:
    print("No existe")
    #remover dato
killnombre=input("Ingrese nombre a eliminar")
nombres.remove(killnombre)

print(nombres)
