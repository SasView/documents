# Tentative course outline

Overview of features and new in 6.0 (15 min)
* Slides general overview of layout and where to find things
* Note on magnetic/pol beam stuff (not taught here)
* Where to find help

Overview of using basic features (45 min - 1h)
* 1d fit simple (polymer Gaussian coil)
* 1d with structure factor (SDS data)
* Fit with polydispersity
* Impact of resolution smearing
* Correlation function
* P(R) of protein – Apoferritin .. and maybe sphere and rod?
* GSS - with form factor – Apoferritin
* add/multiply used in response to question

Model writing (45 min -1h)
* Simple sin function
* Sphere - write basic equation on board
* Step through
  * Easy editor  and “hand write” all equations including besse NO polydisperse parameters
  * Use scipy functions
  * Use library functions
  * Make polydisperse → point out the need to move 1/V out of the equation and use form_volume. Difference between z average (volume average) and number average
  * Make possible to use structure factor
  * Move to C
  * Add beta approximation (have_fq=true)
  * What if it IS a structure factor?

Brief look at CLI (quick demo of Caitlyn Wolf stuff?) (15 min)

Bonus if time permits: preview of future features to come (beyond 6.0)
