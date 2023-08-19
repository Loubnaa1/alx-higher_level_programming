#!/usr/bin/python3
def weight_average(my_list=[]):
    numerateur = 0
    denominateur = 0

    for x in my_list:
        produit = x[0] * x[1]
        numerateur += produit
        denominateur += x[1]

    if denominateur == 0:
        denominateur = 1

    weighted_average = numerateur / denominateur
    return weighted_average

