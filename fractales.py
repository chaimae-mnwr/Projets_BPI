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
        a1 = (random.uniform(angle-20, angle+20))%360
        a2 = (random.uniform(angle-20, angle+20))%360
        a3 = (random.uniform(angle-20, angle+20))%360
        p1 = (depart[0] + distance*cos((pi*a1)/180), depart[1] + distance*sin((pi*a1)/180))
        p2 = (depart[0] + distance*cos((pi*a2)/180), depart[1] + distance*sin((pi*a2)/180))
        p3 = (depart[0] + distance*cos((pi*a3)/180), depart[1] + distance*sin((pi*a3)/180))
        dessine_segment(depart, a1, distance)
        dessine_segment(depart, a2, distance)
        dessine_segment(depart, a3, distance)
        return (dessine_arbre(p1, a1, distance*9/10, n-1),
                dessine_arbre(p2, a2, distance*9/10, n-1),
                dessine_arbre(p3, a3, distance*9/10, n-1))



def main():
    """On génère un SVG kaléidoscopique à partir d'un nombre de triangles"""
    if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], "nombre_arbres > image2.svg")
        sys.exit(1)

    nombre_arbres = int(sys.argv[1])
    print(svg.genere_balise_debut_image(800, 800))
    print(svg.genere_balise_debut_groupe("black", "none", 3))
    dessine_arbre((400,400), 270, 50, nombre_arbres)
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())

if __name__ == "__main__":
    main()
