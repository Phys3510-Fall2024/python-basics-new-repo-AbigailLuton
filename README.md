[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/LvykrN4z)
# Python Basics

In this task, we'll explore some of the foundational elements of Python programming, focusing on native Python features. This assignment is designed to be completed using Jupyter Notebooks, which will allow you to run and test your code interactively.

## Objectives

By the end of this assignment, you will:

1. Understand and use basic arithmetic operations in Python.
2. Assign and manipulate variables.
3. Numerical Types, Strings, and Type Checking
4. Use basic comparison and logical operators.
5. Seek help in Python using built-in functions.
6. Manage and interpret some common error messages.
7. Use several special characters (`;`, `\`, `{}`, `()`, and `[]`) in basic Python code.

## Getting Started

Clone this repository to your local machine and open the provided Jupyter Notebook (`python_basics.ipynb`).

## Assignment -- Part 1: Work through the Jupyter Notebook

## Assignment -- Part 2: Creating a Conversion Dictionary

Objective:
The goal of this assignment is to create a simple Python dictionary that stores conversion factors between different descriptors of waves  and a Boolean flag indicating whether the relationship between the units is an inverse relationship.

Part 0: Basic equations being used

The relationship between a waves characteristic length (or inverse length) and its frequency (or period) is called a dispersion relation. This can also be extended to energy quantities.

For light in vacuum, some common ways of expressing this dispersion relation are:

    $f = c/\lambda$ : the linear frequency is related to the wavelength, $\lambda$, by the speed of light, $c$. 
    
    $\omega = c k$ : the angular frequency is related to the angular wavevector/wavenumber, $k$, by the speed of light. 
    
    $\lambda/T = c$ : here $T$ is the period.  
    
    $E = h f = \hbar \omega = \hbar c k $ : here $h$ is Planck's constant and $\hbar$ is the reduced Planck's constant.  
    
    $k = 2 \pi \nu$ : $\nu$ is the linear wavenumber.  

Check the units to help you remember these dispersion relations.

Part 1: Understanding the Units

1. Units to Consider:

    THz: terahertz (Frequency)
    ps: picoseconds (Period)
    cm⁻¹: inverse centimeters (Wavenumber)
    nm: nanometers (Wavelength)
    meV: millielectronvolts (energy) 

Part 2: Conversion Relationships and Factors

2. Conversion Relationships: Use the dispersion relations to find how the various units are related

    Linear Frequency to Period (THz to ps): Inverse relationship: $T = 1/f$
    Angular Frequency to Wavenumber (THz to cm⁻¹): Direct relationship: $k = \omega/c$
    Linear Frequency to Wavelength (THz to nm): Inverse relationship: $\lambda = c/f$

Part 3: Creating the Dictionary

3. Dictionary Construction:

Your task is to create a Python dictionary that includes the following, for the units described above:

    A tuple as the key, representing the units to convert between (e.g., ("THz", "ps")).
    A value that is another tuple containing:
        The conversion factor (a number).
        A Boolean True or False indicating whether the conversion is inverse.


```python
# Conversion factors and inverse relationship flag
conversion_factors = {
    ("THz", "ps"): (1, True),                # Linear Frequency to Period (inverse; T=1/f)
    ("ps", "THz"): (1, True),                # Period to Linear Frequency (inverse; f=1/T)
    ("THz", "cm-1"): (33.356, False)         # Linear Frequency to Linear Wavenumber (k = f/c)
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
```

