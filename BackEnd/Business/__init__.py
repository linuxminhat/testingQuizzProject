def singleton(class_):
    _instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in _instances:
            _instances[class_] = class_(*args, **kwargs)
        return _instances[class_]

    return get_instance