from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import Div, AutocompleteInput
from bokeh.plotting import figure

import styles
from components import MyCheckbox


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


def create_container_element(label):
    def callback(attr, old, new):
        # nonlocal button, name
        # global DATA, line_cpu, line_mem

        # line_cpu.data_source.data = DATA[name]["cpu"]
        # circle_cpu.data_source.data = DATA[name]["cpu"]
        # line_mem.data_source.data = DATA[name]["mem"]
        global log

        print(attr, old, new)

        log.text = "clicked!"

    cbox = MyCheckbox(label=label)
    cbox.on_change("active", callback)

    return cbox


# Components
cmp_containers = column(
    width=300,
    sizing_mode="stretch_height",
    styles={"padding": "1% 2.5%", "overflow-y": "scroll"},
)
cmp_containers_search = AutocompleteInput(
    completions=["hello", "world", "lorem", "ipsum", "dolor", "sit", "amet"],
    max_completions=10,
    min_characters=2,
    case_sensitive=False,
    styles={"width": "100%", "margin": "7.5px auto"},
)
cmp_containers_list = column(
    sizing_mode="stretch_height",
    styles={"width": "100%"},
)

cmp_containers.children.append(cmp_containers_search)
cmp_containers.children.append(cmp_containers_list)

for i in range(2):
    cmp_containers_list.children.append(create_container_element(f"container-id-{i+1}"))

# for i in range(10):
# cmp_containers_list.children.append(create_container_element("container-id-1"))
# cmp_containers_list.children.append(create_container_element("container-id-2"))


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
log = Div(text="None")
right_container = column(sizing_mode="stretch_height", styles={"width": "14%"})
right_container.children.append(log)
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
