### This code holds a class which models the letters patent pertaining to a
### given peerage.

# Local imports.
import constants

# The class in question.
class Patent_Peerage:
  def __init__(self, ramno, day, month, year, grantee, gender, degree,
               title, subsidiary_titles, whereas, remainder):
    self.ramno = ramno
    self.day = self.get_ordinal(day)
    self.month = month
    self.year = self.get_ordinal(year)
    self.grantee = grantee
    self.gender = gender
    self.degree = degree
    self.title = title
    self.subsidiary_titles = self.get_subsidiary_titles(subsidiary_titles)
    self.whereas = self.get_whereas(whereas)
    self.pronoun_nominative = self.get_pronoun_nominative()
    self.pronoun_dative = self.get_pronoun_dative()
    self.pronoun_possessive = self.get_pronoun_possessive()
    self.advance_clause = self.get_advance_clause()
    self.trusty_clause = self.get_trusty_clause()
    self.state_clause = self.get_state_clause()
    self.dignify_clause = self.get_dignify_clause()
    self.third_invocation = self.get_third_invocation()
    self.remainder = self.get_remainder(remainder)
    self.rights_clause = self.get_rights_clause()
    self.degree_clause = self.get_degree_clause()
    self.degree_plural = self.get_degree_plural()

  # Looks up the result in "constants.py".
  def get_ordinal(self, n):
    result = constants.ordinals[n]
    return result

  # Builds the subsidiary titles string.
  def get_subsidiary_titles(self, inputs):
    result = ""

    if inputs == None:
      return result

    for title in inputs:
      if inputs.index(title) == len(inputs)-2:
        result = result+title+" "
      elif inputs.index(title) == len(inputs)-1:
        result = result+"and "+title+", "
      else:
        result = result+title+", "

    return result

  # Adds an hspace, if necessary
  def get_whereas(self, whereas):
    result = ""

    if ((whereas == None) or (whereas == "")):
      return result
    else:
      result = "\hspace{20pt} "+whereas

    return result

  # Looks up the result in "constants.py".
  def get_pronoun_nominative(self):
    return constants.pronouns_nominative[self.gender]

  # Looks up the result in "constants.py".
  def get_pronoun_dative(self):
    return constants.pronouns_dative[self.gender]

  # Looks up the result in "constants.py".
  def get_pronoun_possessive(self):
    return constants.pronouns_possessive[self.gender]

  # Looks up the result in "constants.py".
  def get_advance_clause(self):
    if self.degree == "baronet":
      return constants.advance_clauses["baronet"]
    else:
      return constants.advance_clauses["peer"]

  # Looks up the result in "constants.py".
  def get_trusty_clause(self):
    if self.degree == "baronet":
      return ""
    else:
      return constants.trusty_clauses[self.degree]

  # Looks up the result in "constants.py".
  def get_state_clause(self):
    if self.degree == "baronet":
      return constants.state_clauses["baronet"]
    else:
      return constants.state_clauses["peer"]

  # Looks up the result in "constants.py".
  def get_dignify_clause(self):
    if ((self.degree == "duke") or (self.degree == "marquess") or
        (self.degree == "earl")):
      if self.gender == "female":
        result = constants.dignify_clauses["female"]+self.title+", "
      else:
        return constants.dignify_clauses[self.degree]
    else:
      return ""

  # Constructs the third invocation of the title granted.
  def get_third_invocation(self):
    if ((self.degree == "duke") or (self.degree == "marquess")):
      result = ("the said name, state, degree, style, dignity, title and "+
                "honour of "+self.title)
    elif self.degree == "earl":
      result = ("the said name, degree, style, dignity, title and honour "+
                "of "+self.title)
    else:
      result = ""

    return result

  # Looks up the result in "constants.py", or not.
  def get_remainder(self, remainder):
    if remainder in constants.standard_remainders.keys():
      result = constants.standard_remainders[remainder]
    else:
      result = remainder

    result = result.replace("#POSSESSIVE", self.pronoun_possessive)
    return result

  # Looks up the result in "constants.py".
  def get_rights_clause(self):
    if self.degree == "baronet":
      return constants.rights_clauses["baronet"]
    else:
      return constants.rights_clauses["peer"]

  # Looks up the result in "constants.py".
  def get_degree_clause(self):
    return constants.degree_clauses[self.degree]

  # Looks up the result in "constants.py".
  def get_degree_plural(self):
    return constants.degrees_plural[self.degree]
