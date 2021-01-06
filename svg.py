"""
Un module pour générer des images au format SVG.

Ce module fournit diverses fonctions pour générer des éléments SVG
sous forme de chaînes de caractères.
Ces chaînes DOIVENT être écrites dans un fichier en respectant la
structure SVG pour obtenir une image valide.
"""

from collections import namedtuple

# Definition de la structure Point composée de deux attributs x et y
Point = namedtuple('Point', 'x y')

def genere_balise_debut_image(largeur, hauteur):
    """
    Retourne la chaine de caractères correspondant à la balise ouvrante pour
    décrire une image SVG de dimensions largeur x hauteur pixels. Les paramètres
    sont des entiers.

    Remarque : l’origine est en haut à gauche et l’axe des Y est orienté vers le
    bas.
    """
    balise = "<svg xmlns='http://www.w3.org/2000/svg' version='{version}' " \
             "width='{largeur}' height='{hauteur}'>"
    return balise.format(version="1.1",
                         largeur=largeur,
                         hauteur=hauteur)

def genere_balise_fin_image():
    """
    Retourne la chaine de caractères correspondant à la balise svg fermante.
    Cette balise doit être placée après tous les éléments de description de
    l’image, juste avant la fin du fichier.
    """
    return "</svg>"

def genere_balise_debut_groupe(couleur_ligne, couleur_remplissage, epaisseur_ligne):
    """
    Retourne la chaine de caractères correspondant à une balise ouvrante
    définissant un groupe d’éléments avec un style particulier. Chaque groupe
    ouvert doit être refermé individuellement et avant la fermeture de l’image.

    Les paramètres de couleur sont des chaînes de caractères et peuvent avoir
    les valeurs :
    -- un nom de couleur reconnu, par exemple "red" ou "black" ;
    -- "none" qui signifie aucun remplissage (attention ici on parle de la chaîne
        de caractère "none" qui est différente de l'objet None).

    Le paramètre d’épaisseur est un nombre positif ou nul, représentant la
    largeur du tracé d'une ligne en pixels.
    """
    balise = "<g stroke='{ligne}' fill='{remplissage}' stroke-width='{epaisseur}'>"
    return balise.format(ligne=couleur_ligne,
                         remplissage=couleur_remplissage,
                         epaisseur=epaisseur_ligne)

def genere_balise_fin_groupe():
    """
    Retourne la chaine de caractères correspondant à la balise fermante pour un
    groupe d’éléments.
    """
    return "</g>"

def genere_cercle(centre, rayon):
    """
    Retourne la chaine de caractères correspondant à un élément SVG représentant
    un cercle (ou un disque, cela dépend de la couleur de remplissage du groupe
    dans lequel on se trouve).

    centre est une structure de données de type Point, et rayon un nombre de
    pixels indiquant le rayon du cercle.
    """
    balise = "<circle cx='{x}' cy='{y}' r='{r}' />"
    return balise.format(x=centre.x,
                         y=centre.y,
                         r=rayon)
                         
def genere_segment(dep, arr):
    ligne = "<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}'/>"
    return  ligne.format(x1=dep[0],
                         y1=dep[1],
                         x2=arr[0],
                         y2=arr[1])
                         
                         
def genere_polygone(points, couleur, stroke):
    
    chainep = " "
    for i in range(0,len(points)):
         chainep = chainep+str(points[i][0])+","+str(points[i][1])+" "
    triangle = "<polygon points='{points}' fill='{remplissage}' stroke ='{stroke}' />"
          
    return  triangle.format(points=chainep, remplissage=couleur, stroke=stroke)

def genere_texte_debut(points,texted):
    texte = "<text x='{x}' y='{y}' fill='{fill}' >"
    return texte.format(x=points[0],
                        y=points[1],
                        fill="rgb(200,0,0)")
                        

def genere_texte_fin():
    return "</text>"
                        
def genere_balise_debut_groupe_transp(niveau_opacite):
    balise = "<g fill-opacity='{niveauopacite}'>"
    return balise.format(niveauopacite=niveau_opacite)
    
def genere_balise_fin_groupe_transp():
    return "</g>"
                                                    
