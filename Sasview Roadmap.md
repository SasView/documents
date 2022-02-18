# SasView 5 Year Roadmap 

The purpose of building and operating large scattering facilities is to provide unique tools to answer new scientific questions with the final presentation of results (usually in the form of a paper) as the output. The biggest obstacle to that output is often the analysis of the acquired data. Data analysis software has been variously viewed as being in the domain of the scientist using the facility, a service to be provided by scattering facilities, or as the individual responsibility of the scientists running the facility beamlines. The result has been a proliferation of packages and libraries, many written and supported by one key person, often not as their primary responsibility [^1]. 

Over the past decade several trends have contributed to exacerbate the analysis bottleneck: 1) As the techniques have matured the user pool has broadened.  This combined with an apparent decrease in the overall level of programming taught to scientists, means that fewer users are capable of building their own analysis tools.  2) With the increasing maturity of the field, a large amount of basic modeling is well understood and developed.  Even those capable of coding their own should not be wasting their time re-inventing the wheel but focus on new science and perhaps new analysis developments to enable that new science. 3) The quantity of data being produced by instruments and the complexity of the experiments being performed have increased. 4) Finally, as the general software landscape has moved towards increased quality of usability and support, users of scattering facilities, in particular new users, have similar expectations of the software they use to operate the instrument and process and analyse their data.

To enable the production and maintenance of software that meets users expectations, a greater level of resources needs to be applied to the problem. This has been recognised in the neutron scattering community through projects such as DANSE [^2], Mantid [^3], CCPSAS[^4] and projects within the European Union Horizon 2020 programme such as SINE2020[^5]. While each facility or scientist may not be able to commit the necessary resources, pooling of expertise between facilities and with the user community into a single project can amplify the effort and provide gains in quality, functionality, longevity and supportability with obvious benefits to both the facilities and the users.

The aim of the SasView project is to provide open source, *collaboratively developed software for the analysis of small angle scattering data*

The collaborative development model is designed to encourage and enable contribution from a range of experts in small angle scattering, computer science and software development. Users of the software are encouraged to participate through bug reports, submitting code and by integrating their own scattering models.

This is a regularly updated document, reviewed at each Code Camp. Document history is maintained and previous iterations can be found in the SasView GitHub repository[^6]

[^1]: <http://smallangle.org/content/Software>

[^2]: <http://www.danse.us/>

[^3]: <http://www.mantidproject.org>

[^4]: <http://www.ccpsas.org> 

[^5]: <http://sine2020.eu>

[^6]: <http://github.com/SasView/documents/Roadmap>

[^7]: <https://github.com/SASfit/SASfit>

[^8]: <http://www.esrf.eu/UsersAndScience/Experiments/CRG/BM26/SaxsWaxs/DataAnalysis/Scatter>

[^9]: <https://github.com/usnistgov/pyPRISM>

## Development Model

The SasView project is co-ordinated by a small management team who are also members of the broader development team. The development team currently consists of scientists and software engineers from scattering facilities around the world. Progress is monitored and project direction discussed at bi-weekly video conferences. The work is divided into various work packages that bundle together related tasks and issues. The project aims for a major release each year, with minor bug fix releases as required in between.

The source code for SasView is hosted on GitHub, allowing anyone to fork the code base, add functionality or fix bugs, and easily request that the code be merged into the project. The use of unit tests and code quality metrics is employed to help manage the contribution of code from a varied and dispersed developer base.

As of 2015, few if any of the developers have SasView as a major component of their job assignments. Given the nature of software development this currently means most development occurs during annual code camps.  While this has proven to be a highly successful approach, it limits the rate of progress.  The Roadmap presented below is intended to give guidance to the development team and to our stakeholders as to the direction we aim to take over the next 5 years. It is an optimistic one predicated on more resources becoming available, either through new developers joining the project or work on SasView becoming a greater part of the day-to-day assignment for the current developers. It also should be used as a source of ideas for projects that could be undertaken with short-term resources or to meet specific requirements of stakeholders if they have the necessary resources available.

## Roadmap

Every release should include bug fixes and new models as requests come in.  These are assumed with each release and not included specifically below.  Likewise general robustness and ease of use issues will be addressed in each release cycle.

**Late 2021 to mid 2022 Release 5.0.5**

Subject to the availability of sufficient resources, release 5.0.5. Work will start on refactoring fitting to allow, for example custom re-parameterization of models (e.g. replace SLD with fraction of solvent in layer), using an input array for P or S in a P*S model, fitting oriented model to 1D cut etc. Work will begin on refactoring the simultaneous/constrained fitting workflow interface and on custom workflows identified as highest priority and having a well developed design.  Work on new workflow/interfaces for contrast variation for example and new magnetic scattering workflows will begin. User documentation/tutorials will be reviewed, an advanced "how to fit my data" tutorial will be started, and an architecture manual begun.

Task Summary (Subject to the availability of sufficient resources):

* Begin model fitting refactoring work to allow custom re-parameterization of models, allow reading in an array representing either PQ or SQ for P*S fits, fitting oriented model to 1D cuts including revisiting orientation definitions etc.
* Complete architecture manual
* Begin work on refactoring constrained/simultaneous fits.
* Begin work on adding custom workflows identified as highest priority 
* Work to update tutorials to support 5.x
* Begin work on advanced model fitting tutorial
* Complete work to refactor/improve generic scattering calculator
* Complete SasView paper
* Create plan for developing community interactions.
* Begin work on incorporating polyhedral form factors
* Continue work on graphical represtation of models
* Begin work on SAXS/SANS co-refinement
* Begin work on incorporating generic resolution functions
* Usual bug fixes and other minor improvements as time and interest permit

**Late 2022 - Mid 2023 - Release 5.1**

Subject to the availability of sufficient resources, release 5.1 will provide new fitting functionality such as custom re-parameterization of models, allow reading in an array representing either PQ or SQ for P*S, fitting oriented model to 1D cut etc. The refactored workflow interfaces for constrained/simultaneous fits and batch fitting and plotting module will be deployed in this release.  Work will continue on an advanced data fitting with SasView tutorial.  These workflows are not expected to be in the release however. Work on providing the generic O-Z solver tool that is present in SASFit will begin. Work on support for multi-GPU and multi-CPU computation, which may involve refactoring away from OpenCL as support for this standard is waning. Incorporation of the PRISM[^9] (polymer reference interaction site model) code into SasView. McSAS and FFSAS will be integrated into SasView, giving users an approach to obtaining particle size distributions.

Task Summary (Subject to the availability of sufficient resources):

* Finish fitting refactoring work to allow custom re-parameterization of models, allow reading in an array representing either PQ or SQ for P*S fits, fitting oriented model to 1D cut etc.
* Refactor simultaneous/constrained workflow interface
* Integration of McSAS and FFSAS
* Begin work on generic O-Z solver
* Inclusion of PRISM[^9] functionality
* Continue development of advanced fitting tutorial
* Start new workflow/interfaces
* Support for multi-GPU, multi-CPU and CPU/GPU computation
* Finish work on O-Z solver.
* Extend generic scattering calculator with SPONGE and McSim.
* Complete work on refactor/improve P(R) inversion
* Complete work on SAXS/SANS co-refinement
* Complete work on incorporating generic resolution functions
* Community meeting at SAS2022
* Usual bug fixes and other minor improvements as time and interest permit

**Late 2023 - Mid 2024  - Release 5.2**

Subject to the availability of sufficient resources, release 5.2 will again try place an emphasis on addressing requests for smaller feature enhancements and improvements to the interface and workflow.  It will also include some new workflow interfaces.  Use cases and design development will commence on a web interface (possibly including smartphone app capabilities). Advanced fitting tutorial and other unfinished documentation projects will be completed. Review all documentation and prioritize needs for next release. Work on integration of SasView into realtime analysis workflows at beamlines will begin.

Task Summary (Subject to the availability of sufficient resources):

* Finish advanced model fitting tutorial
* Include more workflow/interfaces
* Begin use case and design on Web interface (with possible smartphone app feature) * initial version can have minimal features but would be useful for demos?
* Finish outstanding documentation projects
* Prioritize new documentation tasks
* Usual bug fixes and other minor improvements as time and interest permit
* Headless operation/realtime analysis workflows started


**Late 2024 - Mid 2025 - Release 5.3 / Release 6.0 alpha/beta**

Subject to the availability of sufficient resources, release 5.3 will start providing intelligent feedback on unreasonable choices.  Transition will start to the 6.x release series as support for ASAXS is added and other SAXS specific tools/workflows are added as needed.  Web UI work will continue but is not expected to be ready for this release.  Finally work will begin to allow computational code to run on a cluster and an intelligent launcher/scheduler design started for the GUI frontend which will make the use of the a cluster backend transparent to the user. Include documentation tasks prioritized in previous round. Integration of SasView into a realtime analysis workflow on beamlines will be completed.

Task Summary (Subject to the availability of sufficient resources):

* Start including intelligent limits/help (possibly include switch between enforcement and warning only) and explore the use of wizards in some cases
* Continue work on web UI and smartphone app
* ASAXS support added 
* Add extra SAXS specific needs as appropriate
* Enable computational code to run on clusters and refactor GUI to add an intelligent launcher/scheduler that makes the use of a cluster back end transparent to the user
* Documentation tasks as determined during previous code camp or fortnightly meetings
* Headless operation and realtime analysis workflows completed.
* Usual bug fixes and other minor improvements as time and interest permit

**Late 2025 - Mid 2026 - Release 6.0**

Subject to the availability of sufficient resources, release 6.0 will allow running compute intensive portions of SasView computation on a cluster back end with a transparent access from the user GUI.  It will also allow deployment as a webservice with a web based front end which will have limited functionality in this first instance.  ASAXS and other SAXS specific workflows will be included. Work on a smartphone app interface to the webservice will continue but lilkely will not be ready for this release. The use of wizards and intelligent user guidance will be expanded and new workflows/interfaces may be added as appropriate. Include documentation tasks prioritized in previous round.

Task Summary (Subject to the availability of sufficient resources):

* UI refactoring complete
* Deploy computational code on clusters
* GUI includes intelligent launcher/scheduler that makes the use of a cluster back end transparent to the user
* Deploy Web application
* Expand use of wizards and intelligent user guidance
* Add new workflow interfaces as appropriate
* Continue work on smartphone UI
* Documentation tasks as determined during previous code camp or fortnightly meetings
* Usual bug fixes and other minor improvements as time and interest permit

**Late 2026 - Mid 2027 - Release 6.x**

Subject to the availability of sufficient resources, release 6.x will again try place an emphasis on addressing requests for smaller feature enhancements and improvements to the interface and workflow.  It will also continue to expand on intelligent guidance and include more functionality on web app and see the deployment of a smartphone app. Include documentation tasks prioritized in previous round.

* Continue to expand use of wizards and intelligent user guidance
* Deploy smartphone app
* Expanded functionality of web app
* Documentation tasks as determined during previous code camp or fortnightly meetings
* Usual bug fixes and other minor improvements as time and interest permit



## Revision History ##

* 2015-11-24	: First release
* 2016-10-11	: Updated after Code Camp V discussions
* 2018-09-07 : Updated after Code Camp VI & VII discussions
* 2022-02-18 : Updated after magnetic SANS discussions
