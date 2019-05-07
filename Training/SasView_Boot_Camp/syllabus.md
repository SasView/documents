Outline
=======
* Day One = Using SasView
  * morning = overview lectures
  * Afternoon = hands-on/tutorial
* Day Two = Write your own model - hands-on
* Day Three = using sasview via scripting interface 
  * Morning = Python tutorial
  * Afternoon = Intro to scripting with Jupyter Notebook and using to script sasview
* Day Four = Contribute - BOOT CAMP! (preparation for code camp)
  * includes contributing to tutorials, documentation, checking and fixing math, adding tests, reporting using issues, GUI framework code, marketplace database, etc. 

DAY ONE - Using SasView
=======================

## Morning: OVERVIEW
* General overview of SasView (40 + 20 questions)
* Overview of functionality and demos etc (3h)
  * Overview of menu items with some demos
  * Tools for learning/using
  * Website
  * Help docs
  * model docs/help
  * Tutorials
  * Github repo
  * Wiki information and tickets
  * social media :-)
  * Community development model  - all skills -- reporting bugs .. and fixing

## Afternoon: Hands on usage/tutorial
* How to do a fit
* Simple fit
* P*Q
* Batch fitting
* Constrained fitting
* Other perspectives (PR, invariant, corfunc) and tools (image, genscatt, )

DAY TWO - Model writing
=======================

## Lectures
* Introduction to model structure and infrastructure
* Sasmodels vs sasview
* Model definition vs infrastructure
* Plugin model concepts
* Builders (sum/multiply) vs Editors
* Intro to documentation to writing plugins
* Basic structure of model definitions
* Writing model all the way to upload to marketplace
## Hands On - build your own model
* **Step 1:** Preparation
  * Read paper and pull out equations and write down
  * Choose what your parameters should be
* **Step 2:** enter all in python to using new model editor
  * Enter parameters
  * Enter equations
  * save/test
  * Test how it behaves in SasView
* **Step 3:** fine tune with advanced editor
  * Load model with advanced editor
  * Add things like F(q), VR, ER, flags etc
* **Step 4:** move IQ to C
  * Move xxx.c to plugin directory and rename to be yourmodel.c
  * Move Iq function to c
  * Add source= to python side
  * Add fq to c side
  * Move form volume etc
  * test/save
  * Test how it behaves in SasView
* **Step 5:** Add tests and docs (and tweak model)
  * Follow doc template - Include:
    * Math
    * References
    * Author and date
    * Reviewer and date
    * Last modified and date
  * Add unit tests
    * Add at least 3 tests
    * Include polydispers and 2D if model supports
    * Try to add tests of use cases and some edge cases
    * When possible compare against data in reference.
  * Test models
* **Step 6:** upload to marketplace

DAY THREE - Python and scripting: Deep Dive
===========================================
## Morning - Basic Python intro including exercises

## Afternoon - Scripting
* Intro to Jupiter notebooks including exercises
* Use Jupiter notebook to script sasview and sasmodels
* Introduction to scripting sasview and sasmodels
* Simple exercise
* PR
* corfunc?
* Simple fit
* complicated constrained batch fit

DAY FOUR - Contributing to SasView - giving back to the community: boot camp!
==============================================================================

Tutorials and Setting up
------------------------
* How to collaborate: Learning github and trac
* Overview of git
* Install git on laptops
* Overview of github
* Use git to clone tutorial and sasmodels repos
* Issues, comits and pull requests
* “Advanced git”
* Exercise on ???
* Overview of code layout and different repos (including tutorials)
* Install development environments (what IDE to use + tortoise git?)

Breakouts
---------
* Write a Tutorial
* Make a video for SasView youtube channel
* Review a model (from issue):
 * Take ticket
 * check math, functionality, docs
 * Updated ticket
* Computational Infrastructure - pick a bug
* GUI infrastructure - pick a bug
* Contribute to maintain twitter/facebook/etc??