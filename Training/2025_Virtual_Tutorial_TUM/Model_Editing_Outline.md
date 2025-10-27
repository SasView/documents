## OUTLINE OF MODEL EDITING

*NOTE: PLUGINS ARE BROKEN IN 6.1.1 -- USED 6.1.0 for this*


**SO …. WHAT CAN I DO IF NO MODEL IS ADEQUATE?**
* SASMODELS  MAGIC: THE TWO MAIN INTERFACES
  * From scratch: python (with or without c files)
  * Using existing models as a base
* HAS SOMEBODY ELSE DONE THE WORK?
  * Download octahedron from marketplace
  * Show how to “install” and use via the model manager tool (easy!)
* INTERACTING WITH EXISTING MODELS
  * Sum, multiply - the tool
    * Coreshell sphere+sphere (from magSANS lecture yesterday)
  * More than just 2 models? - editing the file
    * Example sum coreshellsphere + sphere + power law
  * Reparameterize existing – new editor
    * Sphere → replace radius with agg number
    * Test with SDS example data
  * Use PDB to create a plugin model
  * NOTHING ELSE WORKS? DEVELOP FROM SCRATCH - USE EDITOR (see Brayden’s video) - use simple sin equation for example (A sin(wq))
    * Python only
    * Add poly disperse (show and explain how volume parameter works)
    * Add C (note #source [] line and explanation in c template. Can almost copy paste from python if using special functions in python
    * Allow multiply by Sq… OR be an Sq
    * Numpy and scipy are OK. E.G. use numpy.sin or scipy.special.bessel. Import done automatically
