from django_atomics.base import Component


class Container(Component):
    template_string = """
    <div {% if attrs %}{{ attrs }}{% endif %} class="container{% if classes %} {{ classes }}{% endif %}">
        {{ childs }}
    </div>
    """


class Row(Component):
    template_string = """
    <div {% if attrs %}{{ attrs }}{% endif %} class="row{% if classes %} {{ classes }}{% endif %}">
        {{ childs }}
    </div>
    """


class Col(Component):
    template_string = """
    <div {% if attrs %}{{ attrs }}{% endif %} class="col{% if classes %} {{ classes }}{% endif %}">
        {{ childs }}
    </div>
    """


class DropdownItem(Component):
    template_string = """
    <li>
        <a {% if attrs %}{{ attrs }}{% endif %}
            class="dropdown-item" href="{{ url }}"
        >
            {% if icon %}
                <i class="mdi mdi-{{ icon }}"></i>
            {% endif %}
            {{ label }}
        </a>
    </li>
    """


class DropdownDivider(Component):
    template_string = """
    <li><hr class="dropdown-divider"></li>
    """


class DropdownHeader(Component):
    template_string = """
    <li><h6 class="dropdown-header fw-bold">{{ label }}</h6></li>
    """


class Dropdown(Component):
    template_string = """
    <div {% if attrs %}{{ attrs }}{% endif %}
         {% if style %}style="{{ style }}"{% endif %}
         class="dropdown{% if classes %} {{ classes }}{% endif %}"
    >
         <a href="#" class="dropdown-toggle {{ toggle_classes }}"
            id="{{ id }}"
            data-bs-toggle="dropdown"
            aria-expanded="false"
         >
            {% if icon %}
                <i class="mdi mdi-{{ icon }}"></i>
            {% endif %}
            {{ toggle_label }}
         </a>
         <ul class="px-0 dropdown-menu{% if dropdown_classes %} {{ dropdown_classes }}
                                  {% else %} dropdown-menu-end{% endif %}"
             aria-labelledby="{{ id }}">
             {{ childs }}
         </ul>
    </div>
    """
