from abc import ABC, abstractmethod
import pickle
import json


class SerializationInterface(ABC):
    @abstractmethod
    def serilization_json(self, *args, **kwargs):
        pass
    @abstractmethod
    def serilization_bin(self, *args, **kwargs):
        pass

class Serialization(SerializationInterface):
    def serilization_json(self, *args, **kwargs):
        pass
    def serilization_bin(self, *args, **kwargs):
        pass
