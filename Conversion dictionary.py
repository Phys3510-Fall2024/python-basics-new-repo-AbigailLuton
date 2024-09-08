from math import *
#constants
c = 3*10**8 #m/s
h = 6.63*10**-34 #J*s
#Prefixes to consider
#tera--10^12
#pico--10^-12
#centi--10^-2
#nano--10^-9
#Creating dictionary
my_dictionary = {"Wave Conversion": "Python", "version": 3.9}

# Conversion factors and inverse relationship flag
conversion_factors = {
    ("THz", "ps"): (1, True),                # Linear Frequency to Period (inverse; T=1/f)
    ("ps", "THz"): (1, True),                # Period to Linear Frequency (inverse; f=1/T)
    ("THz", "cm-1"): (33.356, False)         # Linear Frequency to Linear Wavenumber (k = f/c)
#Reverse direction
    ("cm-1", "THz"): (.3, False)
#angular frequency to wavenumber: direct relationship k=w/c
    ("THz", "cm-1"): (3e-22, False) #k=w/(3e8(m/s)(100cm/m)(s/10e-12 ps))
#wavenumber to angular frequency: direct relationship w=kc
    ("cm-1", "THz"): (3e22, False) #w=k(3e8(m/s)(100cm/m)(s/10e-12 ps))
#linear frequency to wavelength: inverse relationship l=c/f
    ("THz", "nm"): (3e31, True)
#wavelength to linear frequency: inverse relationship f=c/l
    ("nm", "THz"): (3e31, True)
}

# Example of how to access the dictionary
# Let's say we want to convert from THz to ps
conversion_key = ("THz", "ps")

if conversion_key in conversion_factors:
    factor, is_inverse = conversion_factors[conversion_key]
    print(f"Conversion factor: {factor}")
    print(f"Is inverse relationship: {is_inverse}")
else:
    print("Conversion not supported.")
    