import math

"""
Created on Thu 01 22 00:28:00
@author: MVP
"""

""" 
THIS SCRIPT SHOULD CONTAIN FUNCTIONS TO QUICKLY AND EFFECTIVLY CALCULATE
WAVELENGTHS AND DISTANCE MEASUREMENTS IN ACCORDANCE TO THE BEUGUNG 05
EXPERIMENTS AND QUESTIONAIRRE
INTRODUCTION
THE PHYSICS
OUR BASIS FORMULAE ARE;
(1) SIN(THETA) = (N*LAMBDA)/ G
THETA: CURVATURE ANGLE
LAMBDA: WAVELENGTH
N: ORDER NUMBER
G: MATRIXCONSTANT
(2) TAN(THETA) = DK/D
THETA: CURVATURE ANGLE, AS USED IN (1)
DK:DISTANCE FROM 0. MAXIMA TO K. MAXIMA ON YOUR PROJECTION
D: DISTANCE FROM YOUR MATRIX TO YOUR PROJECTION SCREEN
"""


def wavelength(d_proj=1, m=1):
    """
    Alles in m eingeben
    Relevant zur Berechnung Aufgabe 4
    Kleinwinkelnäherung:
    g: Gitterkonstante in micrometer
    d_1: Abstand 0. zu 1. Maxima in centimeter
    d_proj: Abtand Gitter zum Schirm in meter default: d_proj=1m
    Allgemein:
    theta: beugungswinkel
    m:ordnungszahl default: m=1
    Fehlereinschätzung mit Gausschen Fehlerfortpflanzung
    """

    try:
        g = input('Input Gitterkonstante in micrometer:\n')
        d_1 = input('Input d_1 in cm:\n')
    except NameError as ne:
        print('Something went wrong')
        print(ne)

    try:
        d_1 = float(d_1)*(10**(-2))  #convert d_1 from cm to m
        g = float(g)*(10**(-6))  #convert g from micrometer to m
    except TypeError as tp: #value error if '' entered
        print('Please enter a proper value')
        print(tp)

    theta = math.atan(d_1/d_proj)  #curvature angle

    wavelength_kn = (g*d_1) / (d_proj)
    wavelength_kn = wavelength_kn * (10**(9))  #show wavelength in nm

    wavelength = (g*math.sin(theta))/m
    wavelength = wavelength*(10**(9))  # in nm angeben

    #Gauss Uncertainty for Kleinwinkelnäherung

    #delta_lambda = input('Unsicherheit für Wellenlänge in cm:\n')

    delta_g = float(input('Input Unischerheit für g-Wert in micrometer:\n'))
    delta_d_1 = float(input('Input Unischerheit für d1-Wert in centimeter:\n'))
    delta_d_proj = float(input('Input Unischerheit für d_proj-Wert in centimeter:\n'))

    #idea for later. make it able to sense unit input and be flexible for multi inputs

    #deltas in m

    delta_g = delta_g*(10**(-6))
    delta_d_1 = delta_d_1*(10**(-2))
    delta_d_proj = delta_d_proj*(10**(-2))

    #Ableitungen für Kleinwinkelnäherung

    ddg = d_1/d_proj
    ddd_1 = g/d_proj
    ddd_proj = (-g*d_1) / (d_proj**2)

    term_g = (ddg*delta_g)**2
    term_d_1 = (ddd_1*delta_d_1)**2
    term_d_proj = (ddd_proj*delta_d_proj)**2

    delta_lambda = math.sqrt(term_g + term_d_1 + term_d_proj)

    delta_lambda = delta_lambda*(10**(9))  #in nm eingeben


    print(f'Die Wellenlänge Lambda unter Kleinwinkelnäherung beträgt {wavelength_kn} ± { delta_lambda} nm')
    print(f'Die Wellenlänge Lambda unter normalen Bedingungen beträgt {wavelength} ± N/A nm')

    return wavelength_kn, delta_lambda


def gitterkonstant(wave_lambda=532, m=1):
    """
    This should help you solve Aufgabe 5, or any question that involved
    needing to calculate the g-value.
    This can stand for the dimensions of a hole,
    or the uniform distance between holes in a matrix.
    wave_lambda: Wellenlänge Lambda default:532 for ND:Yg Laser
    d_1: Abstand zwischen Maxima in Abbildung auf Schirm
    d_proj: Abstand zwischen Gitter und Schirm
    """
    #inputs

    try:
        d_proj = input('Input Schirmabstand in centimeter:\n')
        d_1 = input('Input d_1 in cm:\n')
    except NameError as ne:
        print('So..something went wrong')
        print(ne)

    #treat iputs

    try:
        d_1 = float(d_1)
        d_proj = float(d_proj)
    except TypeError as te:
        print('Enter something caclculable')
        print(te)

    wave_lambda = wave_lambda*(10**(-9))  #wavelength in m
    d_1 = d_1*(10**(-2))  #cm to m
    d_proj = d_proj*(10**(-2))  #cm to m

    theta = math.atan(d_1/d_proj)  #bending angle

    #gitter value
    g = wave_lambda / math.sin(theta)

    g = g*(10**(6))  #in um angeben

    #Gaussian Fehlerfortpflanzung
    if wave_delta:
        delta_wave = wave_delta
    else:
        delta_wave = float(input('Input Unischerheit für lambda-Wert in nanometer:\n'))
    
    try:
        delta_d_1 = float(input('Input Unischerheit für d1-Wert in centimeter:\n'))
        delta_d_proj = float(input('Input Unischerheit für d_proj-Wert in centimeter:\n'))
    except ValueError as ve: 
        print('Yo motherfucker do a better job at using my script')
        print(ve)

    #idea for later. make it able to sense unit input and be flexible for multi inputs

    #deltas in m

    delta_wave = delta_wave*(10**(-9))
    delta_d_1 = delta_d_1*(10**(-2))
    delta_d_proj = delta_d_proj*(10**(-2))

    #Ableitungen für Kleinwinkelnäherung

    dd_lambda = 1 / math.sin(theta)
    ddd_1 = (-wave_lambda*math.cos(theta)) / ((1+(d_1/d_proj)**2)*d_proj*((math.sin(theta))**2))
    ddd_proj = (wave_lambda*d_1*math.cos(theta)) / ((d_proj**2)*(1+((d_1/d_proj)**2))*((math.sin(theta))**2))

    term_lambda = (dd_lambda*delta_wave)**2
    term_d_1 = (ddd_1*delta_d_1)**2
    term_d_proj = (ddd_proj*delta_d_proj)**2

    delta_g = math.sqrt(term_lambda + term_d_1 + term_d_proj)

    delta_g = delta_g*(10**(6))  #in micrometer angeben

    print(f'Die Gitterkonstante g beträgt {g}±{delta_g}um')

    return g


prompt_wavelength = input('Are you solving for the wavelength lambda as in Aufgabe 4? Enter to skip\n')

if prompt_wavelength:

    wave_lambda , wave_delta = wavelength()

prompt_g = input('Are you solving for a Gitterkonstante g? Enter to skip\n')

if prompt_g:

    prompt_use = input('Do you want to use your Lambda from the previous calculation? Enter to skip and use Data Sheet value.\n')
    if prompt_use:
        try:
            g = gitterkonstant(wave_lambda=wave_lambda) 
        except NameError as ne:
            print('Seems like you didn’t calculate a wavelength in the previous prompt.')
            print(ne)
    else:
        g = gitterkonstant()