import csv
import pandas as pd

archivo_csv = 'datos_prueba_tecnica.csv'

# Leer el archivo CSV en un DataFrame de pandas
empleados_df = pd.read_csv(archivo_csv, delimiter=';')


#Punto 1: Indicamos cuantos hombres y mujeres hay del total de los empleados:

hombres = empleados_df[empleados_df['sexo'] == 'H'].shape[0]
mujeres = empleados_df[empleados_df['sexo'] == 'M'].shape[0]

print(f"La cantidad de hombres es: {hombres}")
print(f"La cantidad de mujeres es: {mujeres}")


# Punto 2: Indicamos la suma de salario bruto anual de los empleados en la empresa 1 (Equilibrha IT) y el centro de trabajo CT2 (Alovera)

salario_bruto = empleados_df[(empleados_df['ID Empresa'] == 1) & (empleados_df['ID Centro trabajo'] == 'CT2')]

suma_salario_bruto = salario_bruto['salario bruto anual'].sum()

print(f"\nLa suma del total bruto anual de los empleados de la empresa 1 centro de trabajo CT2 es: {suma_salario_bruto}")




#Punto 3: listado de empleados (id empleado, nombre, apellidos, salario y empresa) que cobren más de 28000 euros y que pertenezcan a la empresa 2 (Equilibra RRHH)

# Filtramos los empleados de la empresa 2 (Equilibra RRHH) con salario mayor a 28000
empleados_filtrados = empleados_df[(empleados_df['ID Empresa'] == 2) & (empleados_df['salario bruto anual'] > 28000)]

# Imprimimos listado de empleados (id empleado, nombre, apellidos, salario y empresa)
print("\nListado de empleados que cobran más de 28000 euros y pertenecen a la empresa 2 (Equilibra RRHH):")
for index, row in empleados_filtrados.iterrows():
    print(f"ID Empleado: {row['id empleado']}, Nombre: {row['nombre']}, Apellidos: {row['apellido1']} {row['apellido2']}, Salario: {row['salario bruto anual']}, Empresa: {row['Nombre empresa']}")
