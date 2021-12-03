from django.utils.html import format_html_join


def flatatt(attrs):
    """
    Convert a dictionary of attributes to a single string.
    The returned string will contain a leading space followed by key="value",
    XML-style pairs. In the case of a boolean value, the key will appear
    without a value. It is assumed that the keys do not need to be
    XML-escaped. If the passed dictionary is empty, then return an empty
    string.

    The result is passed through 'mark_safe' (by way of 'format_html_join').
    """
    key_value_attrs = []
    boolean_attrs = []
    for attr, value in attrs.items():
        if isinstance(value, bool):
            if value:
                boolean_attrs.append((attr,))
        elif value is not None:
            key_value_attrs.append((attr, value))

    return format_html_join("", ' {}="{}"', sorted(key_value_attrs)) + format_html_join(
        "", " {}", sorted(boolean_attrs)
    )


def flatstyle(style):
    """
    Convert a dictionary of attributes to a single string.
    The returned string will contain property:value; CSS Style.
    The result is passed through 'mark_safe' (by way of 'format_html_join').
    """

    prop_values = []
    for property, prop_value in style.items():
        prop_values.append((property, prop_value))
    return format_html_join("", '{}:{}; ', sorted(prop_values))


def construct_template_name(template_name):
    return template_name
