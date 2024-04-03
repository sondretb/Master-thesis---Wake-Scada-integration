from py_wake.literature.noj import Jensen_1983
from py_wake.literature.gaussian_models import Bastankhah_PorteAgel_2014
from py_wake.utils.plotting import setup_plot
from py_wake.deflection_models import JimenezWakeDeflection, DeflectionModel
from py_wake.deficit_models.deficit_model import DeficitModel
from siemens6MW import Siemens6MW
from py_wake.site import UniformSite
import matplotlib.pyplot as plt


def plot_flowmap_demo(deficit_model: DeficitModel, deflection_model: DeflectionModel, yaw=None):
    if yaw:
        wt_x = [100*i for i in len(yaw)]
        wt_y = [0*i for i in len(yaw)]
    else:
        yaw=[0]

    print(wt_x, wt_y)

    windTurbines = Siemens6MW()
    site = UniformSite()

    wfm = deficit_model(site=site, windTurbines=windTurbines, deflection_model=deflection_model)


    sim_res = wfm([0], [0])


    # Plot wake map

    plt.figure(wfm.__class__.__name__, figsize=(6, 3))
    plt.title("Wake deficit model: " + wfm.__class__.__name__)

    flow_map = sim_res.flow_map(wd=[270])
    flow_map.plot_wake_map()
    flow_map.plot_windturbines()

    plt.show()


