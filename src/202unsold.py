#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## 202-unsold
## File description:
## 202unsold
##

from sys import stderr, argv

def error():
    if (len(argv) != 3):
        print("retry with -h", file=stderr)
        exit (84)
    try:
        int(argv[1])
        int(argv[2])
    except Exception as error:
        print(error, file=stderr)
        exit (84)
    if (int(argv[1]) <= 50 or int(argv[2]) <= 50):
        print("a and b must be greater than 50", file=stderr)
        exit(84)
    
                
def help():
    if len(argv) >= 2 and argv[1] == "-h":
        print("USAGE\n    ./202unsold a b\n")
        print("DESCRIPTION\n    a     constant computed from past results")
        print("    b     constant computed from past results")
        exit (0)
    error()

def print_ligne(y, a, b):
    tab = []
    x = 10
    for i in range(1, 6):
        x = i * 10
        tab.append(((a - x) * (b - y)) / (((5 * a) - 150) * ((5 * b) - 150)))
    return tab

def print_law(a, b):
    tab = []
    y = 10
    for i in range(1, 6):
        y = i * 10
        tab.append(print_ligne(y, a, b))
    return (tab)

def get_law_z(z, a, b):
    res = 0
    for y in range(1, 6):
        for x in range(1, 6):
            result = ((a - x * 10) * (b - y * 10)) / (((5 * a) - 150) * ((5 * b) - 150))
            if (x + y == z):
                res += result
    return res

def esperencevariance(xlaw, ylaw, zlaw):
    esp_x = 0
    esp_y = 0
    esp_z = 0
    variance_x = 0
    variance_y = 0
    variance_z = 0
    coeff = 10
    for x in xlaw:
        esp_x += x * coeff
        coeff += 10
    coeff = 10
    for y in ylaw:
        esp_y += y * coeff
        coeff += 10
    coeff = 20
    for z in zlaw:
        esp_z += z * coeff
        coeff += 10
    coeff = 10
    for vx in xlaw:
        variance_x += vx * pow((coeff - esp_x), 2)
        coeff += 10
    coeff = 10
    for vy in ylaw:
        variance_y += vy * pow((coeff - esp_y), 2)
        coeff += 10
    coeff = 20
    esp_z *= 1 / sum(zlaw) 
    for vz in zlaw:
        variance_z += vz * pow((coeff - esp_z), 2)
        coeff += 10
    variance_z *= (1 / sum(zlaw))
    print("expected value of X:\t%.1f" % esp_x)
    print("variance of X:\t\t%.1f" % variance_x)
    
    print("expected value of Y:\t%.1f" % esp_y)
    print("variance of Y:\t\t%.1f" % variance_y)
    
    print("expected value of Z:\t%.1f" % esp_z)
    print("variance of Z:\t\t%.1f" % variance_z)
    print ("--------------------------------------------------------------------------------")
    
def print_tab(tab):    
    print ("\tX=10\tX=20\tX=30\tX=40\tX=50\tY law")
    nb = 10
    y_law = []
    x_law = []
    z_law = []
    for x in tab:
        print("Y=%d" % nb, end='')
        for y in x:
            print("\t%.3f" % y, end='')
        print("\t%.3f" % (sum(x)))
        y_law.append(sum(x))
        nb += 10
    print("X law", end='')
    for i in range(5):
        res = sum(x[i] for x in tab)
        x_law.append(res)
        print("\t%.3f" % (res), end='')
    print("\t1.000")
    z = 2
    print ("--------------------------------------------------------------------------------")
    print("z\t20\t30\t40\t50\t60\t70\t80\t90\t100\np(Z=z)", end='')
    for z in range(2, 11):
        print("\t%0.3f" % (get_law_z(z, int(argv[1]), int(argv[2]))), end='')
        z_law.append(get_law_z(z, int(argv[1]), int(argv[2])))
    print("\n--------------------------------------------------------------------------------")
    esperencevariance(x_law, y_law, z_law)
        
    
if __name__=="__main__":
    help()
    print ("--------------------------------------------------------------------------------")
    tab = print_law(int(argv[1]), int(argv[2]))
    print_tab(tab)
    exit(0)