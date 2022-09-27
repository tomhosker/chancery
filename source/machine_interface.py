"""
This code defines a machine interface class, with which code can create and use
an object of the Patent-type class.
"""

# Standard imports.
import json

# Local imports.
from .patent import Patent
from .patent_peerage import PatentPeerage

##############
# MAIN CLASS #
##############

class MachineInterface:
    """ The class in question. """
    # Class attributes.
    PATENT_TYPE_KEY = "type"
    PEERAGE_TYPE = "peerage"

    def __init__(self, path_to_input_file):
        self.path_to_input_file = path_to_input_file
        self.patent_obj = self.make_patent_object()

    def make_patent_object(self):
        """ Make the patent object, given the input file. """
        with open(self.path_to_input_file, "r") as input_file:
            input_dict = json.loads(input_file.read())
        patent_type = input_dict.pop(self.PATENT_TYPE_KEY)
        if patent_type == self.PEERAGE_TYPE:
            result = PatentPeerage(**input_dict)
        else:
            result = Patent(**input_dict)
        return result

    def generate(self):
        """ Generate the output. """
        self.patent_obj.generate()
