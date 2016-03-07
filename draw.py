from display import *

def add_point(matrix, x, y, z=0):
    matrix.append([x, y, z, 1])
    #matrix.append(['0', '0', '0', '0']) #placeholder

def add_edge(matrix, x0, y0, z0, x1, y1, z1):
    matrix.append([x0, y0, z0, 1])
    matrix.append([x1, y1, z1, 1])
	
def draw_matrix(matrix, screen, color):
    for i in range(len(matrix) - 1):
        draw_line( screen, matrix[i][0], matrix[i][1], matrix[i+1][0], matrix[i+1][1], color )
        #if (matrix[i][0] != '0'): #placeholder to separate connected lines from points or other connected lines.
        #    if (matrix[i+1][0] == '0'): #is a point
        #        plot(screen, color, matrix[i][0], matrix[i][1])
        #    else: #is a line
        #        draw_line( screen, matrix[i][0], matrix[i][1], matrix[i+1][0], matrix[i+1][1], color )
    save_ppm( screen, "Test1.ppm" )

def draw_line( screen, x0, y0, x1, y1, color ):
    if x1 < x0:
        x0, x1 = x1, x0
        y0, y1 = y1, y0 #that was easy
    #now every line goes from left to right and there are only 4 octants to deal with.
    if (y1 >= y0): #if positive slope
        if y1 - y0 > x1 - x0: #if slope > 1
            dx = x1 - x0
            dy = y1 - y0
            dxTimes2 = dx * 2
            dxTimes2MinusdyTimes2 = 2 * (dx - dy)
            k = (dx * 2) - dy
            x = x0
            for y in range (y0, y1 + 1):
                if (k < 0):
                    k += dxTimes2
                    plot(screen, color, x, y)
                else:
                    k += dxTimes2MinusdyTimes2
                    x += 1
                    plot(screen, color, x, y)
        else: #if slope <= 1
            dx = x1 - x0
            dy = y1 - y0
            dyTimes2 = dy * 2
            dyTimes2MinusdxTimes2 = 2 * (dy - dx)
            k = (dy * 2) - dx
            y = y0
            for x in range (x0, x1 + 1):
                if (k < 0):
                    k += dyTimes2
                    plot(screen, color, x, y)
                else:
                    k += dyTimes2MinusdxTimes2
                    y += 1
                    plot(screen, color, x, y)
    else: #negative slope
        if y0 - y1 > x1 - x0: #if slope > -1
            y0, y1 = -1*y0, -1*y1
            dx = x1 - x0
            dy = y1 - y0
            dxTimes2 = dx * 2
            dxTimes2MinusdyTimes2 = 2 * (dx - dy)
            k = (dx * 2) - dy
            x = x0
            for y in range (y0, y1 + 1):
                if (k < 0):
                    k += dxTimes2
                    plot(screen, color, x, -1*y)
                else:
                    k += dxTimes2MinusdyTimes2
                    x += 1
                    plot(screen, color, x, -1*y)
        else: #if slope < -1
            y0, y1 = -1*y0, -1*y1
            dx = x1 - x0
            dy = y1 - y0
            dyTimes2 = dy * 2
            dyTimes2MinusdxTimes2 = 2 * (dy - dx)
            k = (dy * 2) - dx
            y = y0
            for x in range (x0, x1 + 1):
                if (k < 0):
                    k += dyTimes2
                    plot(screen, color, x, -1*y)
                else:
                    k += dyTimes2MinusdxTimes2
                    y += 1
                    plot(screen, color, x, -1*y)
    save_ppm( screen, "Test1.ppm" )