from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import (
    Div,
    Button,
    InlineStyleSheet,
    AutocompleteInput,
    CheckboxGroup,
)
from bokeh.plotting import figure

import styles
from components import Checkbox


DATA = {
    "container-id-1": {
        "cpu": {
            "x": [0, 1, 2, 3],
            "y": [5, 5, 10, 80],
        },
        "mem": {
            "x": [0, 1, 2, 3],
            "y": [5, 5, 10, 20],
        },
    },
    "container-id-2": {
        "cpu": {
            "x": [0, 1, 2, 3],
            "y": [8, 8, 15, 25],
        },
        "mem": {
            "x": [0, 1, 2, 3],
            "y": [5, 5, 10, 20],
        },
    },
}


def create_container_element(name):
    def callback():
        nonlocal button, name
        global DATA, line_cpu, line_mem

        line_cpu.data_source.data = DATA[name]["cpu"]
        circle_cpu.data_source.data = DATA[name]["cpu"]
        line_mem.data_source.data = DATA[name]["mem"]

    style = InlineStyleSheet(
        css="""
        .bk-btn {
            font-family: Raleway;
            padding: 10px 0;
        }"""
    )
    button = Button(
        label=name,
        button_type="primary",
        stylesheets=[style],
        styles={"width": "100%", "margin": "5px 0"},
    )
    button.on_click(callback)

    return button


# Components
cmp_containers = column(
    width=300,
    sizing_mode="stretch_height",
    styles={"padding": "1% 0", "overflow-y": "scroll"},
)
cmp_containers_search = AutocompleteInput(
    completions=["hello", "world", "lorem", "ipsum", "dolor", "sit", "amet"],
    max_completions=10,
    min_characters=2,
    case_sensitive=False,
    styles={"width": "85%", "margin": "5px auto"},
)
cmp_containers_list = column(
    sizing_mode="stretch_height",
    styles={"width": "85%", "margin": "5px auto"},
)

# style_cbtn = InlineStyleSheet(css="""label input {size: 10px}""")
# cbtn = CheckboxGroup(labels=["a", "b", "c"], stylesheets=[style_cbtn])

# style_checkbox = InlineStyleSheet(
#     css="""
#     .container {
#         display: block;
#         position: relative;
#         cursor: pointer;
#         -webkit-user-select: none;
#         -moz-user-select: none;
#         -ms-user-select: none;
#         user-select: none;
#     }
#     .container input {
#         position: absolute;
#         cursor: pointer;
#         opacity: 0;
#         height: 0;
#         width: 0;
#     }
#     .checkmark {
#         position: relative;
#         display: inline-block;
#         height: 25px;
#         width: 25px;
#         background-color: #eee;
#         vertical-align: middle;
#     }
#     .container:hover input ~ .checkmark {
#         background-color: #ccc;
#     }
#     .container input:checked ~ .checkmark {
#         background-color: #2196F3;
#     }
#     .checkmark:after {
#         content: "";
#         position: absolute;
#         display: none;
#     }
#     .container input:checked ~ .checkmark:after {
#         display: block;
#     }
#     .container .checkmark:after {
#         left: 9px;
#         top: 5px;
#         width: 7px;
#         height: 14px;
#         border: solid white;
#         border-width: 0 3px 3px 0;
#         -webkit-transform: rotate(45deg);
#         -ms-transform: rotate(45deg);
#         transform: rotate(45deg);
#     }
#     .container .label {
#         display: inline-block;
#         margin-left: 7.5px;
#         vertical-align: middle;
#         font-size: 16px;
#         font-family: Raleway;
#         cursor: pointer;
#     }
#     """
# )
# checkbox_div = Div(
#     text="""
# <label class="container">
#     <input type="checkbox" id="checkbox" name="checkbox">
#     <span class="checkmark"></span>
#     <label class="label" for="checkbox">Option 1</label>
# </label>
# """,
#     stylesheets=[style_checkbox],
# )
# checkbox_div2 = Div(
#     text="""
# <label class="container">
#     <input type="checkbox" id="checkbox" name="checkbox">
#     <span class="checkmark"></span>
#     <label class="label" for="checkbox">Option 2</label>
# </label>
# """,
#     stylesheets=[style_checkbox],
# )

cb = Checkbox(label="container-id-1")
cb2 = Checkbox(label="container-id-2")

cmp_containers.children.append(cmp_containers_search)
cmp_containers.children.append(cb)
# cmp_containers.children.append(cb2)
cmp_containers.children.append(cmp_containers_list)

for i in range(10):
    cmp_containers_list.children.append(create_container_element("container-id-1"))
    cmp_containers_list.children.append(create_container_element("container-id-2"))


# Create the middle plots
tooltips = [("x", "@x"), ("y", "@y")]

plot1 = figure(title="CPU", sizing_mode="stretch_both", tooltips=tooltips)
line_cpu = plot1.line(x=[], y=[], color="blue", line_width=2)
circle_cpu = plot1.circle(
    x=[],
    y=[],
    size=7,
    color=styles.palette[3],
    line_color=styles.palette[2],
    # fill_alpha="alpha",
)
# line_cpu_lim = plot1.line(x=[], y=[], color="blue", line_width=2, line_dash="dashed")

plot2 = figure(title="Memory", sizing_mode="stretch_both")
line_mem = plot2.line(x=[], y=[], color="green", line_width=2)

middle_container = column(
    plot1,
    plot2,
    sizing_mode="stretch_both",
    styles={"padding": "0.5% 1% 1% 1%"},
)

# Create the right container
right_container = column(sizing_mode="stretch_height", styles={"width": "14%"})
# right_container.children.append(
#     Div(
#         width=320,
#         height=800,
#     )
# )

# Add the containers to the layout
layout = row(
    cmp_containers,
    middle_container,
    right_container,
    sizing_mode="stretch_both",
    stylesheets=[styles.scrollbar],
)

# Add the layout to the document
curdoc().add_root(layout)
curdoc().title = "Docker Stats UI"
