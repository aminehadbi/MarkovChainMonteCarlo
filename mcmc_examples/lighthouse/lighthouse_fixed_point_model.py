from spinn_utilities.overrides import overrides

from data_specification.enums.data_type import DataType

from mcmc.mcmc_model import MCMCModel
from mcmc.mcmc_parameter import MCMCParameter
from mcmc.mcmc_state_variable import MCMCStateVariable


class LightHouseFixedPointModel(MCMCModel):
    """ MCMC Model for the lighthouse problem, using fixed point
    """

    def __init__(
            self, alpha_jump_scale, alpha_min, alpha_max, beta_jump_scale,
            beta_min, beta_max):
        """
        :param alpha_jump_scale:\
            scaling of t transition distribution for MH jumps in alpha\
            direction
        :param alpha_min: The minimum value of alpha
        :param alpha_max: The maximum value of alpha
        :param beta_jump_scale:\
            scaling of t transition distribution for MH jumps in beta direction
        :param beta_min: The minimum value of beta
        :param beta_max: The maximum value of beta
        """

        self._alpha_jump_scale = alpha_jump_scale
        self._alpha_min = alpha_min
        self._alpha_max = alpha_max
        self._beta_jump_scale = beta_jump_scale
        self._beta_min = beta_min
        self._beta_max = beta_max

    @overrides(MCMCModel.get_binary_name)
    def get_binary_name(self):
        return "lighthouse.aplx"

    @overrides(MCMCModel.get_parameters)
    def get_parameters(self):
        return [
            MCMCParameter(self._alpha_jump_scale, DataType.S1615),
            MCMCParameter(self._beta_jump_scale, DataType.S1615),
            MCMCParameter(self._alpha_min, DataType.S1615),
            MCMCParameter(self._alpha_max, DataType.S1615),
            MCMCParameter(self._beta_min, DataType.S1615),
            MCMCParameter(self._beta_max, DataType.S1615)
        ]

    @overrides(MCMCModel.get_state_variables)
    def get_state_variables(self):
        return [
            MCMCStateVariable("alpha", 0.0, DataType.S1615),
            MCMCStateVariable("beta", 1.0, DataType.S1615)
        ]
