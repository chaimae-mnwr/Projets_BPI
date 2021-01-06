import random
import svg
import sys
from math import cos
from math import sin
from math import pi

def dessine_segment(point, angle, distance):
    x = point[0]
    y = point[1]
    nx = distance*cos((pi*angle)/180)
    ny = distance*sin((pi*angle)/180)
    print(svg.genere_segment((x,y), (x+nx,y+ny)))
    return 0





def dessine_arbre(depart, angle, distance, n):
    """Dessine un arbre recursivement"""
    if n == 0 :
        dessine_segment(depart, angle, distance)
        return 0
    else :
        a1 = (random.uniform(angle-30, angle+30))%360
        a2 = (random.uniform(angle-30, angle+30))%360
        a3 = (random.uniform(angle-30, angle+30))%360
        p1 = (depart[0] + distance*cos((pi*a1)/180), depart[1] + distance*sin((pi*a1)/180))
        p2 = (depart[0] + distance*cos((pi*a2)/180), depart[1] + distance*sin((pi*a2)/180))
        p3 = (depart[0] + distance*cos((pi*a3)/180), depart[1] + distance*sin((pi*a3)/180))
        dessine_segment(depart, a1, distance)
        dessine_segment(depart, a2, distance)
        dessine_segment(depart, a3, distance)
        return (dessine_arbre(p1, a1, distance*9/10, n-1),
                dessine_arbre(p2, a2, distance*9/10, n-1),
                dessine_arbre(p3, a3, distance*9/10, n-1))

SORTIE_STANDARD = False

# On choisit où est-ce que l'on va faire nos prints
if SORTIE_STANDARD:
    out = sys.stdout
else:
    out = open("mon_image2.svg", "w")

print(svg.genere_balise_debut_image(100, 100))
print(svg.genere_balise_debut_groupe("black", "none", 3))

dessine_arbre((0,0), 270, 40, 10)

print(svg.genere_balise_fin_groupe())
print(svg.genere_balise_fin_image())
