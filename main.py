import csv

archivo_csv = 'datos_prueba_tecnica.csv'


empleados = []


with open(archivo_csv, mode='r', encoding= 'utf-8') as file: 

    lector_csv = csv.reader(file, delimiter= ';')

    encabezado = next(lector_csv)


    for linea in lector_csv:
        empleados.append(linea)

#for element in empleados:
    #   print(element)


    #Punto 1: Indicamos cuantos hombres y mujeres hay del total del empleado

    hombres = sum(1 for empleado in empleados if empleado[4] == 'H')
    mujeres = sum(1 for empleado in empleados if empleado[4] == 'M')

    print(f"La cantidad de hombres es: {hombres}")
    print(f"La cantidad de mujeres es: {mujeres}")

    #Punto 2: Indicamos la suma de salario bruto anual de los empleados en la empresa 1 (Equilibrha IT) y el centro de trabajo CT2 (Alovera)

    salario_bruto = sum(int(empleado[6]) 
                        for empleado in empleados if empleado[7] == '1' and empleado[9] == 'CT2')

    print (f"\n La suma del total bruto anual de los empleados de la empresa 1 centro de trabajo CT2 es: {salario_bruto}")


# Punto 3: Crear e imprimir un listado de empleados que cobren más de 28000 euros y pertenezcan a la empresa 2 (Equilibra RRHH)

empleados_filtrados = []


for empleado in empleados:
    if empleado[7] == '2' and int(empleado[6]) >28000:
        empleados_filtrados.append(empleado)


# Imprimimos el  listado de empleados que cobren más de 28000 euros y que pertenezcan a la empresa 2 (Equilibra RRHH)
print("\n Empleados que cobran más de 28000 euros y pertenecen a la empresa 2 (Equilibra RRHH):")
for empleado in empleados_filtrados:
    print(f"ID Empleado: {empleado[0]}, Nombre: {empleado[1]}, Apellidos: {empleado[2]} {empleado[3]}, Salario: {empleado[6]}, Empresa: {empleado[8]}")