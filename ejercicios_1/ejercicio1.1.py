#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#promedio de duracion
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100

print(f"el curso de dalto dura {diferencia_con_min}% menos que el curso mas rapido")
