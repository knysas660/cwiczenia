#python_lst257.py

#Nie uruchamiać
#tylko pokazuje przykład nie kod

#Rysowanie figur
#bez poliformizmu

shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    if type(a_shape) == 'Triangle':
        a_shape.draw_triangle()
    if type(a_shape) == 'Sqare':
        a_shape.draw_sqare()
    if type(a_shape) == 'Circle':
        a_shape.draw_circle()

#Rysowanie figur
#z wykorzystaniem poliformizmu

shapes = [tr1,
          sq1,
          cr1]
for a_shape in shapes:
    a_shape.draw()

