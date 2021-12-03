from django_atomics.component import Component


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
