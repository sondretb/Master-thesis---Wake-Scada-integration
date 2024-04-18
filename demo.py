from py_wake.literature.noj import Jensen_1983
from py_wake import BastankhahGaussian
from py_wake.literature.gaussian_models import Bastankhah_PorteAgel_2014
from py_wake.turbulence_models import STF2017TurbulenceModel
from py_wake.utils.plotting import setup_plot
from py_wake.deflection_models import JimenezWakeDeflection, DeflectionModel
from py_wake.turbulence_models import TurbulenceModel
from py_wake.deficit_models.deficit_model import DeficitModel
from siemens6MW import Siemens6MW
from py_wake.site import UniformSite
import matplotlib.pyplot as plt
from py_wake.examples.data.iea37._iea37 import IEA37Site
from py_wake.examples.data.hornsrev1 import V80
import pandas as pd
from dudgeon import WT_X, WT_Y



def plot_flowmap_demo(deficit_model: DeficitModel, deflection_model: DeflectionModel, turbulence_model: TurbulenceModel, yaw=None, ws=10, wd=270):
    if yaw:
        turbine_amount = len(yaw)
        wt_x = [1000*i for i in range(turbine_amount)]
        wt_y = [0*i for i in range(turbine_amount)]
    else:
        yaw=[0]

    if not turbulence_model:
        plot_turbulence = False
        print("can't plot turbulence, no model specified")
    else:
        turbulenceModel = turbulence_model()

    windTurbines = V80()
    site = IEA37Site()
    D = windTurbines.diameter()

    wfm = deficit_model(site=site, windTurbines=windTurbines, deflectionModel=deflection_model(), turbulenceModel = turbulenceModel)

    sim_results = wfm(x=wt_x, y=wt_y, ws=ws, wd=wd, yaw=yaw, tilt=0)


    flow_map = sim_results.flow_map()
    print(sim_results.to_dataframe())
    

    # Plot wake map
    plt.figure(wfm.__class__.__name__, figsize=(4*turbine_amount, 4))
    plt.title("Wake deficit model: " + wfm.__class__.__name__)

    if not (wfm.__class__ == Jensen_1983):
        center_line = flow_map.min_WS_eff()
        plt.plot(center_line.x/D, center_line/D,'--k')

    flow_map.plot_wake_map(normalize_with=D)

    if plot_turbulence:
        plt.figure(turbulenceModel.__class__.__name__, figsize=(4*turbine_amount, 4))
        plt.title("Turbulence Model: " + turbulenceModel.__class__.__name__)
        flow_map.plot(flow_map.TI_eff, clabel="Added turbulence intensity [-]", levels=100, cmap="Blues", normalize_with=D)

    plt.show()

def plot_DOW(deficit_model: DeficitModel, deflection_model: DeflectionModel, turbulence_model: TurbulenceModel, yaw=[0 for _ in range(len(WT_Y))], ws=10, wd=270):
    turbine_amount = len(WT_Y)
    
    if len(yaw) != turbine_amount:
        raise Exception(f"Yaw list not of dimention {turbine_amount}.")
    
    if not turbulence_model:
        plot_turbulence = False
        print("can't plot turbulence, no model specified")
    else:
        turbulenceModel = turbulence_model()
        plot_turbulence = True

    windTurbines = V80()
    site = IEA37Site()
    D = windTurbines.diameter()

    wfm = deficit_model(site=site, windTurbines=windTurbines, deflectionModel=deflection_model(), turbulenceModel = turbulenceModel)

    sim_results = wfm(x=WT_X, y=WT_Y, ws=ws, wd=wd, yaw=yaw, tilt=0)


    flow_map = sim_results.flow_map()
    print(sim_results.to_dataframe())
    
    # Plot wake map
    plt.figure(wfm.__class__.__name__, figsize=(4, 4))
    plt.title("Wake deficit model: " + wfm.__class__.__name__)


    flow_map.plot_wake_map(normalize_with=D)

    if plot_turbulence:
        plt.figure(turbulenceModel.__class__.__name__, figsize=(4*turbine_amount, 4))
        plt.title("Turbulence Model: " + turbulenceModel.__class__.__name__)
        flow_map.plot(flow_map.TI_eff, clabel="Added turbulence intensity [-]", levels=100, cmap="Blues", normalize_with=D)

    plt.show()

plot_DOW(deficit_model=BastankhahGaussian, 
                  deflection_model=JimenezWakeDeflection, 
                  turbulence_model=STF2017TurbulenceModel,
                  wd=290, ws=5, yaw=[10,10,10]+[ 0 for _ in range(len(WT_Y)-3)])

