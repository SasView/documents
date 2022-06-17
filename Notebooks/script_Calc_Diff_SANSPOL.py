import numpy as np
import math
import matplotlib.pyplot as plt
import os.path
import re
import time
from scipy.spatial.transform import Rotation
from IPython.display import clear_output
from sasmodels.data import load_data
from sas.sascalc.calculator import sas_gen   


qbin=80
qrange=0.02
counter=1
sampleYaw=90
samplePitch=0
sampleRoll=0

#set rotation of sample to yaw 90Deg such that z is along magn field vector at instrument
sampleCoord = Rotation.from_euler("XYZ", [np.radians(sampleYaw), np.radians(samplePitch), np.radians(sampleRoll)])

SLDNuc=6.7e-6#for maghemite

#create mesh of q values for 2Dscattering
q = np.linspace(-qrange, qrange, qbin)
qx, qy = np.meshgrid(q, q)

#function to create file path relative to location of script
def _get_data_path(*path_parts):
    from os.path import realpath, join as joinpath, dirname
    return joinpath(dirname(realpath(__file__)), *path_parts)

for root, dirs, files in os.walk(r'./NF_OMFData'):

    for file in files:
        filename= file.rsplit(".", 1)[0]
        print(str(counter)+" of "+str(len(files))+": "+file)
        #start timer
        t = time.time()

        #Load spatial magnetisation distribution
        #ofpath = _get_data_path("NF_OMFData", file)
        ofpath = "/Users/wojciechpotrzebowski/SASVIEW_WORKSPACE/GSC/A_Raw_Example-1.omf"
        # #check that file exists
        # if not os.path.isfile(ofpath):
        #     raise ValueError("file(s) not found: %r"%(ofpath,))

        #create scattering length density profile model
        oreader = sas_gen.OMFReader()
        omfdata = oreader.read(ofpath) 
        model = sas_gen.GenSAS()
        model.set_sld_data(omfdata)



        model.set_rotations(xyz_to_UVW=sampleCoord)

        #set beam + Nuclear SLD parameter
        model.params['scale'] = 1.0
        model.params['background'] = 1e-7
        model.params['solvent_SLD'] = SLDNuc
        # SANSpol measurement with field perp to beam
        model.params['Up_frac_out'] = 0.5
        model.params['Up_theta'] = 90
        model.params['Up_phi'] = 0



        #calulate scattering for spin up
        print("SANSPOL1")
        model.params['Up_frac_in'] = 1
        result1 = model.runXY([qx, qy])
        #calulate scattering for spin down
        print("SANSPOL0")
        model.params['Up_frac_in'] = 0
        result0 = model.runXY([qx, qy])
        #difference is nuclear-magnetic interference scattering
        result=result1-result0

        #create data list of 2D scattering CS
        mapped = zip(qx.flat,qy.flat,result.flat)
        datalist=list(mapped)
        print("write file for CS difference")
        #Write result
        file = open('Diff_SANSPOL_'+filename+'.dat', 'w')
        file.write("Data columns Qx - Qy - I(Qx,Qy) \n")
        file.write("ASCII data \n")
        for items in datalist:
            file.writelines(re.sub('[(,)]', '', str(items))+"\n")
        file.close()
        elapsed = time.time() -t
        print("The run took "+str(elapsed)+" sec.")
        counter =counter +1

