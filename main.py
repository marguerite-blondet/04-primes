from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Renvoie True si p est un nombre premier, False sinon.
    """
    premier = True
    if p < 2:
        premier = False
    for d in range(2, int(sqrt(p))+1):
        if p % d == 0:
            premier = False
    return premier

#### Fonction principale


def main():
    """
    Programme principal
    Appelle la fonction secondaire isprime
    """
        # Affiche les nombres premiers de 0 à 99
    for n in range(100):
        if isprime(n):
            print(f"{n} est premier")
        else:
            print(f"{n} n'est pas premier")


if __name__ == "__main__":
    main()
