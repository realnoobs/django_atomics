# Django Hookup

Simple Django Hooks.

Install:

```shell
pip install django_hookup
```

Register function:

```python
# myapp.hooks.py
import django_hookup

@django_hookup.register("register_foobar", order=1)
def say_foo(text):
    """Concat foo and given text"""
    return "foo:%s " % text

@django_hookup.register("register_foobar", order=0)
def say_bar(text):
    """Concat bar and given text"""
    return "bar:%s " % text
```

Calling hooks

```python
# myapp.somewhere.py
import django_hookup

hooks = django_hookup.get_hooks("register_foobar")

text = ""
for func in hooks:
    text += func(func.__name__)
print(text)
```

Hooks Admin (Optional)

Add django_hookup in settings.py

```python
# settings.py

INSTALLED_APPS = [
    "example.app",
    "django_hookup",
    # 
    'django.contrib.admin',
    ...
]
```

Add django_hookup.url

```python
# settings.py

urlpatterns = [
    path("admin/hooks/", include("django_hookup.urls")),
    path("admin/", admin.site.urls),
]
```
