from display import *
from draw import *
from matrix import *

screen = new_screen()
mat = []

add_point(mat, 50, 100, 0)
add_point(mat, 120, 101, 0)
add_point(mat, 50, 120, 0)
add_edge(mat, 70, 120, 0, 150, 170, 0)
print_matrix(mat)
draw_matrix(mat, screen, [255, 255, 255])

#tramat = create_translation(50,50,0)
#mat = matrix_multiply(mat, tramat)
#print_matrix(mat)
#draw_matrix(mat, screen, [255, 255, 255])

scalmat = create_scale(1.1, 1.1, 0)
print_matrix(scalmat)
rotmat = create_rotate_z(2)
print_matrix(rotmat)
for i in range(15):
    mat = matrix_multiply(mat, rotmat)
    draw_matrix(mat, screen, [255, 255, 255])
    mat = matrix_multiply(mat, scalmat)
    draw_matrix(mat, screen, [255, 255, 255])

#rotmat = create_rotate_x(80)
#print_matrix(rotmat)
#mat = matrix_multiply(mat, rotmat)
#draw_matrix(mat, screen, [255, 255, 255])

"""
x = 0
y = 0
while (y<500):
    draw_line(screen, 250, 250, x, y, [255, 255, 255] )
    y += 50
while (x<500):
    draw_line(screen, 250, 250, x, y, [255, 255, 255] )
    x += 50
while (y>0):
    draw_line(screen, 250, 250, x, y, [255, 255, 255] )
    y -= 50
while (x>0):
    draw_line(screen, 250, 250, x, y, [255, 255, 255] )
    x -= 50
"""