from json import JSONEncoder

from domain.animals import Animal

class AnimalJsonEncoder(JSONEncoder):
    def default(self, o: Animal):
        try:
            to_serialize = o.to_dict()
            return to_serialize
        except AttributeError:
            return super().default(o)
