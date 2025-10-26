## OUTLINE OF PR AND INVARIANT TUTORIAL


### PR
* Documentation and discussion of what it is, limitations and assumptions and use
* Start with a model sphere (synth data) = sphere_80.txt
  * Use defaults
  * Play with reg cst
  * Play with terms
  * Compute R from Rg
  * EXPLORE BUTTON
* Try latex sphere data
* conalbumin
* Warning: As implemented, the current algorithm seems to fail for vefy LONG objects.

### INVARIANT
* Documentation and what is. Limitations and assumptions
* Synth sphere application (1% vol fraction, sld = 1, sld_solvent = 6, radius = 80 A, background 0.001 cm^-1)
  * NOTE: This file needs to be created. It is not the same as the sphere_80.txt in examples 
  * calculate invariant -> gives ~ 1 vol%
  * Porod Constant (Iq^4 vs q^4)
  * S/V is --> 0.04% calculation from inputs above yields 0.0377%
* Synth sphere with smearing - repeat above


### HOMEWORK
* PR →
  * Apoferitin protein from example_data
* INVARIANT →
  * Use Homework 7 from UD 2025 UD scattering class
