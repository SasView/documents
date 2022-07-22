THINGS TO HAVE OPEN AND READY for demo purposes.
================================================
* This SCRIPT file
* Windows explorer or equivalent
* github.com/SasView/sasmodels
  * Special.py
  * Models directory
* Website (for documentation)
  * Developer sasmodels
  * User documentation “writing plugin models”
  * User documentation “Polydispersity & Orientational Distributions”
* Make sure to have the demo reparameterized model written and tested.
* Make sure to have the demo distribution model written and tested.

NOTE: the emoji 💥 is used to enclose the SHOW statements below. These are places where the speaker shouldb demonstrating
on the screen.

PRESENTATION
============

* Model fitting calculations are all done through the sasmodels package.  This presentation is NOT about the sasmodels in general, but about the API 
presented to the user wishing to integrate a new model so that sasmodels can then do its magic
* API documentation:
  * Most of the detailed API is available in this very long document at https://www.sasview.org/docs/user/qtgui/Perspectives/Fitting/plugin.html
  (documentaion -> User documentation -> Fitting and other Analysis -> Model Fitting -> writing a plugin model - 💥SHOW💥)
  * There is also a “developer’s guide to sasmodels which documents how sasmodels itself works but also provides information on things like
  numerical integrations, model conversions and testing. This is found at https://www.sasview.org/docs/dev/sasmodels-dev/index.html
  (documentaion -> developer documentation -> sasmodels developers guide - 💥SHOW💥)
* Also very useful is a list of C99 functions that have been made available to both python and C models. Using these can make transferring
python code to C fairly simple.  The list is given in the documentation above and can be found in the repo under sasmodels/special.py (💥SHOW💥)
* There are four places one can find the code for models (💥SHOW EACH💥)
  * On Github in the sasmodels repository (githup.com/SasView/sasmodels and then under sasmodels/models. NOTE: library code used by many C models
  can be placed under sasmodels/models/lib
  * In the sasview installed directory
  * On the model marketplace (marketplace.sasview.org).  This contains not only all the contributed models but also the “built-in” ones.
  Those listed as submitted by “sasview” are those delivered with the installer. Also currently all the contributed models are labeled with
  an x, meaning “not reviewed.” The aspiration is that one day they will be reviewed and given a green check as well.
  * custom built (plugin models) usually go in the user's directory under .sasview/plugin_models.  If a model is added here while SasView GUI
  is running, it will not show up in the GUI till the next time the GUI is started. Alternatively one can go to the Fitting menu item and select the
  `Edit Custom Model` (or the `Manage Custom Models` and choose `Edit`) and load the .py file just dumped into the directory. Then hit `Save`.
  If there are no errors that should force the GUI to find the new model
* Firstly we need to dispel a persistent myth/rumor: there is fundamentally zero difference between a plugin model and a “built-in” model
delivered with SasView. There are however differences in how the GUI handles them. In fact some (but not all) of that can be mitigated by
“cheating” and putting a new model into the sasviewX.X program folder rather than in the plugin directory.
* There are two ways to access the sasmodels kernels to create a new model: new models “from scratch” and “derived models.” Derived models
reconfigure existing models using the model_info class rather than provide a new model equation. There are currently two types of derived models:
  * Composite or mixture models
  * Reparameterized models

### COMPOSITE/MIXTURE MODELS
For a simple sum/multiplication/P\*S composition of two model the GUI built in “Sum|multiply” menu item can be used.
For more complicated ones you will need to edit them either in the Edit model editor of the GUI or any ASCII editor.
(💥SHOW WHAT ADD|MULTIPLY PRODUCES AND HOW ONE WOULD EXPAND TO 3 OR MORE - IT IS SIMPLE FEW LINES OF CODE💥)
### REPARAMETERIZE MODEL
* 💥SHOW💥 premade core shell micelle model reparameterized to get vol frac of solvent in shell
* 💥SHOW💥compare to core shell sphere model - note parameter missing and new parameters
### NEW MODELS FROM SCRATCH
* 💥SHOW/DEMO💥 Add model using Amplitude * sin(wq)
  * simple error checking (forget *).
  * Mention polydisperse parameters to be shown later.
  * Numpy functions auto or use scipy.function (scipy will be auto imported)
  * **NOTICE** no SCALE or BACKGROUND (auto added to ALL functions)
* Anatomy of a model -- 💥SHOW SPHERE.PY💥
  * Documentation VERY IMPORTANT ..includes refs and authors etc. ReST and Latex
  * Name (should be same as file name for now)
  * Title (a tool tip more descriptive name)
  * Description (a string that can serve as a shorthand documentation)
  * (default) category (ignored by plugin in GUI) - the series of defined categories in the built-in models will be the list that SasView GUI uses 
  * PARAMETERS
    * The first line gives the format
    * This is a list of lists. Each parameter is a list of
      * Name string (used by GUI)
      * Units string
      * Default value (initial guess - a value)
      * Default min/max for fitting (given as a list of 2 values)
      * Type string. The allowed values are: nothing, volume (special meaning to be described later); SDL, and Orientation.
      * Description string (used by documentation and possibly as a tooltip)
  * THE FUNCTION Iq -- this is the heart of what YOU put in. NOTE: the order of the parameters must be the same as listed in the parameters list.
  This is true for both the python Iq AND the C Iq.
  * TESTS .. very important so that when some well meaning soul comes by a few years from now and tries to improve the code speed/structure they
  don’t accidentally make it give the wrong answer.
* 3 types of models: pure python (example: adsorbed_layer); python and C (example: sphere.py/sphere.c); embedded C
(recommend against .. ugly! example: gaussian_peak at least 5.0.5 and earlier) (💥SHOW EACH EXAMPLE💥)
  * The main difference is in Iq function which becomes a source list (soure = [sss] -- all libraries are listed first and the C module containing the
  Iq is the last in the liest). in the case of the embedded C, the Iq function is written between triple quots like a doc string. 
* Polydispersity - 💥SHOW SPHERE DOCS EQUATION💥:
  * Any paparemeter labelled as type “volume” will tell sasmodels that the parameter can be polydisperse and the GUI will provide options
  for choosing the functional form and how many sigmas to integrate over.
  * NOTE: If you leave the 1/V (i.e. V^2/V = V) in the model the average you will return is the z (or volume weighted) average.  The SasView
  convention is to return the number average (more commonly understandable by many material scientists.  To do this you must:
    * Remove the 1/V from your function (i.e. use V^2)
    * Provide a new function called form_volume (💥SHOW SPHERE.C💥)
* Structure factors
  * So far, the GUI will not allow such plugins models to be multiplied by a structure factor.  For this sasmodels needs to see either an
  ER function (deprecated and only in python) or a radius_effective_modes list in the python file. The latter gives a list of different options
  (with the name that will show in the dropdown in the GUI), each of which needs coding. Said coding goes into the companion C file
  in the radius_efective function. 💥SHOW core_shell_cylinder EXAMPLE FOR MANY OPTIONS💥
  * With this the GUI will still not provide the option of using the Beta approximation when doing a P\*Q.  For that, besides the radius_efftive,
  the python file also needs to set the Fq flag to true.
    * Fq = true (💥SHOW SPHERE💥 -- or core_shell_cylinder) 
  * Finally for the GUI to recognise the model itself to be an S(Q) rather than a P(Q), the structure factor flag needs to be set ⇒
  structure_factor=true (💥SHOW HARD SPHERE💥)
* So far we have only discussed 1D models. In order to provide 2D calculations for anisotropic models, one needs to also write a 2D Iq function.
The 1D calculation should call Iq (or Fq if Fq = true), while the 2D calcualation will call the 2D function. There are two formst of this:
  * Iqab for shapes that have an axis of symmetry (e.g. cylinders and ellipsoids of revolution) 💥SHOW CYLINDER.C💥
  * Iqabc for shapes without an axis of symmetry (e.g. parlellipiped aor prism models. 💥SHOW PARALELLIPIPED.C💥
### EXTRAS
* Polydispersity Functions  - A polydispersity function can be added to any parameter labeled with the type “volume” and an angular distribution
can be added for any parameter labeled with the type “orientation”. Typically a user will choose one of the included distributions.
HOWEVER, The user can also create a custom (or “plugin”) distribution just as they can create a custom model.  This is documented at
the bottom of the page found at https://www.sasview.org/docs/user/qtgui/Perspectives/Fitting/pd/polydispersity.html
(documentation -> User documentation -> Fitting and other Analysis -> Polydispersity and Orientational Distributions - 💥SHOW 💥)
  * Anatomy (💥SHOW💥 a pre created distribution file. Maybe a top hat?)
    * Imports. Import the classes needed for dispersity calculations
    * Documentation.  Looks just like the model documentation. Hopefully it can be added to the documentation created by
    Sphinx in the future but for now just sits in the code
    * Type. the name of the polydispersity function
    * Defaults. This is a dictionary of the defaults for number of points to generate for the integration,
    the number of sigmas over which to integrate and the width of the distribution FWHM (check if true or HWHM?)
    * The _weights function.  This is where the distribution function is coded
  * Activating -  create a directory in .sasmodels called “weights” that is parallel to the plugin_models directory and place
  the new distribution file (mydistribution.py) in that directory. 💥SHOW💥
* **NOTE:** besides using DOCSTRINGS for the model documentation, they should be used at the start of every function and every class.
These will be scraped automatically at build time to create the developer documentation. This is required for long term
sustainable code.
