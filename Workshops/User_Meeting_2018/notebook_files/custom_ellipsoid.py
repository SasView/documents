import sys
#sys.path.append('path_to_sasmodels')

import numpy as np

from bumps.names import *
from sasmodels.core import load_model
from sasmodels.bumps_model import Model, Experiment
from sasmodels.data import load_data, plot_data

# IMPORT THE DATA USED
data = load_data(sys.argv[1])

#setattr(data, 'qmin', 0.0)
#setattr(data, 'qmax', 10.0)

# DEFINE THE MODEL
kernel = load_model('ellipsoid')

pars = dict(scale=0.08, background=35,
        radius_polar=15, radius_equatorial=800,
        sld=.291, sld_solvent=7.105,
        theta=89.9, phi=90,
        theta_pd=0, theta_pd_n=0, theta_pd_nsigma=3,
        phi_pd=0, phi_pd_n=20, phi_pd_nsigma=3,
        radius_polar_pd=0.222296, radius_polar_pd_n=1, radius_polar_pd_nsigma=0,
        radius_equatorial_pd=.000128, radius_equatorial_pd_n=1, radius_equatorial_pd_nsigma=0)

model = Model(kernel, **pars)

# PARAMETER RANGES (ONLY THOSE PARAMETERS ARE FITTED)
model.scale.range(0, inf)
model.background.range(-inf, inf)
#model.sld.range(-inf, inf)
model.sld_solvent.range(-inf, inf)
#model.radius_polar.range(0, inf)
#model.radius_equatorial.range(0, inf)
#model.volfraction.range(0,0.74)
#model.charge.range(0, inf)
#model.temperature.range(0,1000)
#model.concentration_salt.range(0, 1)
#model.dielectconst.range(0,inf)

M = Experiment(data=data, model=model)

problem = FitProblem(M)
