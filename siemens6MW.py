from numpy.core.multiarray import arange as arange
from py_wake.wind_turbines import WindTurbine
from py_wake.wind_turbines.generic_wind_turbines import GenericWindTurbine, SimpleGenericWindTurbine
from py_wake.wind_turbines.power_ct_functions import SimpleYawModel

class Siemens6MW(SimpleGenericWindTurbine):      #Currently Generic
    def __init__(self):
        super().__init__(name="Siemens6MW", diameter=154, hub_height=110, power_norm=6000, ws_cutin=4, ws_cutout=25)

