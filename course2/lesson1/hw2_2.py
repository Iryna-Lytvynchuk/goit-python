classes = []

class Meta(type):
    def __new__(cls, name, *args, **kwargs):
        classes.append({'cls': cls, 'name': name, 'number': len(classes)})
        return type.__new__(cls, name, *args, **kwargs)
 
class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data

 
class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

a, b = Cls1(''), Cls2('')
print(classes)  