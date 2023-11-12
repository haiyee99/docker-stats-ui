from bokeh.models import Checkbox
from bokeh.util.compiler import TypeScript


CODE = """
import {Checkbox, CheckboxView} from "models/widgets/checkbox"
import {label, span, InlineStyleSheet, StyleSheetLike} from "core/dom"


export class MyCheckboxView extends CheckboxView {
  protected checkmark_el: HTMLElement
  protected container_el: HTMLElement

  override stylesheets(): StyleSheetLike[] {
    const checkbox_css = new InlineStyleSheet(`
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
        border-radius: 5px;
        margin-left: -5px;
        background-color: #eee;
        vertical-align: middle;
        transition: background-color 0.15s;
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
      .container .label {
        display: inline-block;
        margin-left: 10px;
        vertical-align: middle;
        font-size: 16px;
        font-family: Raleway;
        cursor: pointer;
      }
    `)

    return [checkbox_css]
  }

  override render(): void {
    super.render()

    // Temporarily remove input & label node
    this.shadow_el.removeChild(this.checkbox_el)
    this.shadow_el.removeChild(this.label_el)
    this.label_el.classList.add("label")

    // Reconstruct component
    this.checkmark_el = span({class: "checkmark"})
    this.container_el = label({class: "container"})
    this.container_el.appendChild(this.checkbox_el)
    this.container_el.appendChild(this.checkmark_el)
    this.container_el.appendChild(this.label_el)    
    this.shadow_el.append(this.container_el)
  }
}


export class MyCheckbox extends Checkbox {
  static {
    this.prototype.default_view = MyCheckboxView
  }
}
"""


class MyCheckbox(Checkbox):
    __implementation__ = TypeScript(CODE)
