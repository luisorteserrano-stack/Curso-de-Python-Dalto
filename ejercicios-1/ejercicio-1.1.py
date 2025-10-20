# Promedio duración cursos Dalto vs otros cursos
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# Duración curso Dalto en formato crudo vs otros cursos
crudo_promedio = 5
crudo_dalto = 3.5

 
# Diferencias de duración
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso *1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

print(diferencia_con_min)
print(f'El curso de Dalto dura un {diferencia_con_min}% menos que el curso más corto de otros cursos.')
print(f'El curso de Dalto dura un {diferencia_con_max}% menos que el curso más largo de otros cursos.')
print(f'El curso de Dalto dura un {diferencia_con_promedio}% menos que el curso promedio.')
print("-----------")

# Para sacar x números decimales cuando utilizamos // que redondea la parte entera
print(10.0 * 100 // 3 / 100)

# Calculamos el porcentaje de tiempo vacío en los cursos
tiempo_vacio_promedio = 100 - (otros_cursos_promedio / crudo_promedio * 100)
tiempo_vacio_dalto = 100 - (dalto_curso * 1000 // crudo_dalto / 10)

print(f'El tiempo vacío promedio en otros cursos es de un {tiempo_vacio_promedio}%')
print(f'El tiempo vacío en el curso de Dalto es de un {tiempo_vacio_dalto}%')
print("-----------")

print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos.")

print(f"Ver 10 horas de otros cursos equivale a ver {dalto_curso  * 100 // otros_cursos_promedio / 10} horas de otros cursos.")
print("-----------")