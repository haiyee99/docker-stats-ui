from bokeh.models import InlineStyleSheet


palette = ("#352F44", "#5C5470", "#B9B4C7", "#FAF0E6")

scrollbar = InlineStyleSheet(
    css="""
    /* width */
    ::-webkit-scrollbar {
        width: 0px;
    }

    /* Track */
    ::-webkit-scrollbar-track {
        box-shadow: inset 0 0 5px grey;
        border-radius: 10px;
    }

    /* Handle */
    ::-webkit-scrollbar-thumb {
        background: #B9B4C7;
        border-radius: 10px;
    }

    /* Handle on hover */
    ::-webkit-scrollbar-thumb:hover {
        background: #5C5470;
    }
    """
)
