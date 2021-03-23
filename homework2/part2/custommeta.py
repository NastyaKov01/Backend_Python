"""Metaclass module"""

class CustomMeta(type):
    """Metaclass that adds prefix 'custom_' """
    def __new__(cls, name, bases, namespace):
        attrs = dict(('custom_' + name, value) for name, value in namespace.items()
                     if name.startswith('__') is False)
        return super().__new__(cls, name, bases, attrs)
