from math import sqrt

def collision_detector(rect_1, rect_2): #modificacion de la funcion clase 12
    for r1, r2 in [(rect_1, rect_2),(rect_2, rect_1)]:
        return point_in_rectangle(r1.topleft, r2) or \
        point_in_rectangle(r1.topright, r2) or \
        point_in_rectangle(r1.bottomright, r2) or \
        point_in_rectangle(r1.bottomleft, r2)
    
def point_in_rectangle(point, rect):
    x, y = point
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom 

# def detectar_colision_cirC(rect_1, rect_2):
#     co = rect_1.center_y - rect_2.center_y
#     ca = rect_1.center_x - rect_2.center_x
#     distance = sqrt(co ** 2 + ca ** 2)
#     r1 = rect_1.width // 2
#     r2 = rect_2 // 2    
#     return distance <= (r1 + r2)

def distancia_entre_puntos(punto_1, punto_2):
    x1, y1 = punto_1
    x2, y2 = punto_2
    return sqrt((y1 - y2)**2 + (x1 - x2)**2)

def distancia_centros_rect(rect_1, rect_2):
    return distancia_entre_puntos(rect_1.center, rect_2.center)

def calcular_radio_rect(rect):
    return rect.width // 2

def detectar_colision_cirC(rect_1, rect_2):
    distance = distancia_entre_puntos(rect_1.center, rect_2.center)
    r1 = calcular_radio_rect(rect_1)
    r2 = calcular_radio_rect(rect_2)    
    return distance <= (r1 + r2)



 
# def collision_detector(rect_1, rect_2):
#     if point_in_rectangle(rect_1.topleft, rect_2) or \
#        point_in_rectangle(rect_1.topright, rect_2) or \
#        point_in_rectangle(rect_1.bottomright, rect_2) or \
#        point_in_rectangle(rect_1.bottomleft, rect_2) or \
#        point_in_rectangle(rect_2.topleft, rect_1) or \
#        point_in_rectangle(rect_2.topright, rect_1) or \
#        point_in_rectangle(rect_2.bottomright, rect_1) or \
#        point_in_rectangle(rect_2.bottomleft, rect_1):
#         return True
#     else:
#         return False

# def collision_detector(rect_1, rect_2): #Segunda modificacion se cambia los dos return, porque tener mas de uno no es buena practica
#     collision = False
#     if point_in_rectangle(rect_1.topleft, rect_2) or \
#        point_in_rectangle(rect_1.topright, rect_2) or \
#        point_in_rectangle(rect_1.bottomright, rect_2) or \
#        point_in_rectangle(rect_1.bottomleft, rect_2) or \
#        point_in_rectangle(rect_2.topleft, rect_1) or \
#        point_in_rectangle(rect_2.topright, rect_1) or \
#        point_in_rectangle(rect_2.bottomright, rect_1) or \
#        point_in_rectangle(rect_2.bottomleft, rect_1):
#         collision =  True
#     return collision
