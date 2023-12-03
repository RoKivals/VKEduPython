class CustomMeta(type):

    def __new__(mcs, name, bases, classdict, **kwargs):
        for key in list(classdict):
            if not (key.startswith('__') and key.endswith('__')):
                classdict[f"custom_{key}"] = classdict.pop(key)

        classdict["__setattr__"] = mcs.__setattr__
        cls = super().__new__(mcs, name, bases, classdict)
        return cls

    def __init__(cls, name, bases, classdict, **kwargs):
        super().__init__(name, bases, classdict, **kwargs)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)

    def __setattr__(self, key, value):
        return object.__setattr__(self, f"custom_{key}", value)
