#e = mc2

def emc(**masas):
    """
    emc: Calcula la energía en base a las masas segun e=mc2
    
    :params: (**masas = (masa1 = valor, masa2 = valor, masa3 = valor, etc))
    :return: La energía .....
    :rtype: float
    """
    c = 300000
    resultado = [{k: v, 'energia':  v*c**2} for k, v in masas.items()]
    return resultado



print(emc(masa1 = 1000, masa2 = 2000, masa3 =3000))