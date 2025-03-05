from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, "es_ES")

# 1. Obtener la fecha y hora actual
print("\nEjercicio 1:")
now = datetime.now()
print(f"La fecha y hora actual es {now}")

# 2. Crear una hora y fecha especificas
specified_date = datetime(2024, 10, 25, 14, 30, 0)
print(f"La fecha y hora especificada es {specified_date}")

# 3. Formatear fechas
# Metodo strftime() para formatear fechas
formatted_date = now.strftime("%A %B %y %H:%M:%S")
print(f"La fecha y hora formateada es {formatted_date}")

# 4. Operaciones con fechas (sumar, restar, multiplicar, dividir dias, horas etc...)
yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer fue {yesterday}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"Manana es {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"Una hora despues es {one_hour_after}")

# 5. Obtener los componentes individuales de una fecha
year = datetime.year
print(f"El año es {year}")

month = datetime.month
print(f"El mes es {month}")

day = datetime.day
print(f"El día es {day}")

# 6. Calcular la diferencia entre 2 fechas
date1 = datetime(2024, 10, 25, 14, 30, 0)
date2 = datetime.now()

difference = date2 - date1
print(f"La diferencia entre las fechas es {difference}")