from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import CanvasGrid, ChartModule, PieChartModule
from .model import EpsteinCivilViolence
from .agent import Citizen, Cop
from mesa.visualization.UserParam import UserSettableParameter

COLORS = {"Quiescent": "#00AA00", "Jailed": "#880000", "Active": "#000000"}

COP_COLOR = "#000000"
AGENT_QUIET_COLOR = "#0066CC"
AGENT_REBEL_COLOR = "#CC0000"
JAIL_COLOR = "#757575"


def citizen_cop_portrayal(agent):
    if agent is None:
        return

    portrayal = {
        "Shape": "circle",
        "x": agent.pos[0],
        "y": agent.pos[1],
        "Filled": "true",
    }

    if type(agent) is Citizen:
        color = (
            AGENT_QUIET_COLOR if agent.condition == "Quiescent" else AGENT_REBEL_COLOR
        )
        color = JAIL_COLOR if agent.jail_sentence else color
        portrayal["Color"] = color
        portrayal["r"] = 0.8
        portrayal["Layer"] = 0

    elif type(agent) is Cop:
        portrayal["Color"] = COP_COLOR
        portrayal["r"] = 0.5
        portrayal["Layer"] = 1
    return portrayal


model_params = {
    "height": 40,
    "width":40,
    "citizen_density": UserSettableParameter("slider", "Citizen Density", 0.7, 0.2, 0.79, 0.1),
    "cop_density": UserSettableParameter("slider", "Cop Density", 0.05, 0.01, 0.19, 0.05),
    "citizen_vision":7,
    "cop_vision":7,
    "legitimacy":UserSettableParameter("slider", "Legitimacy", 0.5, 0.01, 0.99, 0.1),
    "max_jail_term":1000,
    "pre_condition": UserSettableParameter("slider", "Precondition", 0.05, 0.1, 0.2, 0.01),
}
tree_chart = ChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)
pie_chart = PieChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)
canvas_element = CanvasGrid(citizen_cop_portrayal, 40, 40, 480, 480)
server = ModularServer(
    EpsteinCivilViolence, [canvas_element, tree_chart, pie_chart], "Epstein Civil Violence", model_params
)

