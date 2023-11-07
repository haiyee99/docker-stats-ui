from bokeh.models import Div, InlineStyleSheet

_style = InlineStyleSheet(
    css="""
    .container {
        display: block;
        position: relative;
        cursor: pointer;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }
    .container input {
        position: absolute;
        cursor: pointer;
        opacity: 0;
        height: 0;
        width: 0;
    }
    .checkmark {
        position: relative;
        display: inline-block;
        height: 25px;
        width: 25px;
        background-color: #eee;
        vertical-align: middle;
    }
    .container:hover input ~ .checkmark {
        background-color: #ccc;
    }
    .container input:checked ~ .checkmark {
        background-color: #2196F3;
    }
    .checkmark:after {
        content: "";
        position: absolute;
        display: none;
    }
    .container input:checked ~ .checkmark:after {
        display: block;
    }
    .container .checkmark:after {
        left: 9px;
        top: 5px;
        width: 7px;
        height: 14px;
        border: solid white;
        border-width: 0 3px 3px 0;
        -webkit-transform: rotate(45deg);
        -ms-transform: rotate(45deg);
        transform: rotate(45deg);
    }
    .container .label {
        display: inline-block;
        margin-left: 7.5px;
        vertical-align: middle;
        font-size: 16px;
        font-family: Raleway;
        cursor: pointer;
    }
    """
)


# class Checkbox(Div):
#     def __init__(self, label: str):
#         super().__init__(
#             text=f"""
#             <label class="container">
#                 <input type="checkbox" id="checkbox" name="checkbox">
#                 <span class="checkmark"></span>
#                 <span class="label">{label}</span>
#             </label>
#             """,
#             stylesheets=[_style],
#         )


def Checkbox(label: str):
    return Div(
        text=f"""
            <label class="container">
                <input type="checkbox" id="checkbox" name="checkbox">
                <span class="checkmark"></span>
                <span class="label">{label}</span>
            </label>
            """,
        stylesheets=[_style],
    )
