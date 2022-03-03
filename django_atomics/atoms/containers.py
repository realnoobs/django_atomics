from django_atomics.base import Component


class Div(Component):
    template_string = """
    <div {% if attrs %}{{ attrs }}{% endif %}
        {% if style %}style="{{ style }}"{% endif %}
        {% if classes %}class="{{ classes }}"{% endif %}
        >{{ childs }}</div>
    """


class Nav(Component):
    template_string = """
    <nav {% if attrs %}{{ attrs }}{% endif %}
        {% if style %}style="{{ style }}"{% endif %}
        {% if classes %}class="{{ classes }}"{% endif %}
        >{{ childs }}</nav>
    """


class Header(Component):
    template_string = """
    <header {% if attrs %}{{ attrs }}{% endif %}
        {% if style %}style="{{ style }}"{% endif %}
        {% if classes %}class="{{ classes }}"{% endif %}
        >{{ childs }}</header>
    """


class Footer(Component):
    template_string = """
    <footer {% if attrs %}{{ attrs }}{% endif %}
        {% if style %}style="{{ style }}"{% endif %}
        {% if classes %}class="{{ classes }}"{% endif %}
        >{{ childs }}</footer>
    """


class Article(Component):
    template_string = """
    <article {% if attrs %}{{ attrs }}{% endif %}
        {% if style %}style="{{ style }}"{% endif %}
        {% if classes %}class="{{ classes }}"{% endif %}
        >{{ childs }}</article>
    """


class Section(Component):
    template_string = """
    <section {% if attrs %}{{ attrs }}{% endif %}
        {% if style %}style="{{ style }}"{% endif %}
        {% if classes %}class="{{ classes }}"{% endif %}
       >{{ childs }}
    </section>
    """


class UnOrderedList(Component):
    template_string = """
    <ul {% if attrs %}{{ attrs }}{% endif %}
        {% if style %}style="{{ style }}"{% endif %}
        {% if classes %}class="{{ classes }}"{% endif %}
        >{{ childs }}</ul>
    """


class OrderedList(Component):
    template_string = """
    <ol {% if attrs %}{{ attrs }}{% endif %}
         {% if style %}style="{{ style }}"{% endif %}
         {% if classes %}class="{{ classes }}"{% endif %}
         >{{ childs }}</ol>
    """


class ListItem(Component):
    template_string = """
    <li {{ attrs }}
         {% if style %}style="{{ style }}"{% endif %}
         {% if classes %}class="{{ classes }}"{% endif %}
        >{{ childs }}</li>
    """
