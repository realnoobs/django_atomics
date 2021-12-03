from django_atomics.component import Component


class Div(Component):
    template_string = """
    <div {% if attrs %}{{ attrs }}{% endif %}
         class="{% if classes %}{{ classes }}{% endif %}">{{ childs }}</div>
    """


class Nav(Component):
    template_string = """
    <nav {% if attrs %}{{ attrs }}{% endif %}
         class="{% if classes %}{{ classes }}{% endif %}">{{ childs }}</nav>
    """


class Header(Component):
    template_string = """
    <header {% if attrs %}{{ attrs }}{% endif %}
         class="{% if classes %}{{ classes }}{% endif %}">{{ childs }}</header>
    """


class Footer(Component):
    template_string = """
    <footer {% if attrs %}{{ attrs }}{% endif %}
         class="{% if classes %}{{ classes }}{% endif %}">{{ childs }}</footer>
    """


class Article(Component):
    template_string = """
    <article {% if attrs %}{{ attrs }}{% endif %}
         class="{% if classes %}{{ classes }}{% endif %}">{{ childs }}</article>
    """


class Section(Component):
    template_string = """
    <section {% if attrs %}{{ attrs }}{% endif %} class="section{% if classes %} {{ classes }}{% endif %}">
        {{ childs }}
    </section>
    """


class UnOrderedList(Component):
    template_string = """
    <ul {% if attrs %}{{ attrs }}{% endif %}
         class="{% if classes %}{{ classes }}{% endif %}">{{ childs }}</ul>
    """


class OrderedList(Component):
    template_string = """
    <ol {% if attrs %}{{ attrs }}{% endif %}
         class="{% if classes %}{{ classes }}{% endif %}">{{ childs }}</ol>
    """


class ListItem(Component):
    template_string = """
    <li {% if attrs %}{{ attrs }}{% endif %}
         style="{{ style }}",
         class="{% if classes %}{{ classes }}{% endif %}">{{ childs }}</li>
    """
