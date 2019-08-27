### This code holds a class which models a given letters patent of "other"
### type.

# Local imports.
import constants

# The class in question.
class Patent_Other:
  def __init__(self, ramno, day, month, year, filling):
    self.ramno = ramno
    self.day = self.get_ordinal(day)
    self.month = month
    self.year = self.get_ordinal(year)
    self.filling = filling

  # Looks up the result in "constants.py".
  def get_ordinal(self, n):
    result = constants.ordinals[n]
    return result
