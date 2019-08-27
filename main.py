### This code builds a PDF containing a given letters patent.

# Imports.
import os

# Local imports.
import inputs
from patent_peerage import Patent_Peerage
from patent_other import Patent_Other

# Builds "main.tex".
def make_main():
  if inputs.patent_type == "peerage":
    make_main_peerage()
  else:
    make_main_other()

# Continues "make_main" for the grant of a peerage or baronetage.
def make_main_peerage():
  patent = Patent_Peerage(inputs.ramno, inputs.day, inputs.month,
                          inputs.year, inputs.grantee, inputs.gender,
                          inputs.degree, inputs.title,
                          inputs.subsidiary_titles, inputs.whereas,
                          inputs.remainder)
  f = open("base_peerage.tex", "r")
  main = f.read()
  f.close()
  main = main.replace("#RAMNO", str(patent.ramno))
  main = main.replace("#DAY", str(patent.day))
  main = main.replace("#MONTH", patent.month)
  main = main.replace("#YEAR", str(patent.year))
  main = main.replace("#GRANTEE", patent.grantee)
  main = main.replace("#GENDER", patent.gender)
  main = main.replace("#DEGREE", patent.degree)
  main = main.replace("#TITLE", patent.title)
  main = main.replace("#SUBSIDIARY_TITLES", patent.subsidiary_titles)
  main = main.replace("#WHEREAS", patent.whereas)
  main = main.replace("#PRONOUN_NOMINATIVE", patent.pronoun_nominative)
  main = main.replace("#PRONOUN_DATIVE", patent.pronoun_dative)
  main = main.replace("#PRONOUN_POSSESSIVE", patent.pronoun_possessive)
  main = main.replace("#ADVANCE_CLAUSE", patent.advance_clause)
  main = main.replace("#TRUSTY_CLAUSE", patent.trusty_clause)
  main = main.replace("#STATE_CLAUSE", patent.state_clause)
  main = main.replace("#DIGNIFY_CLAUSE", patent.dignify_clause)
  main = main.replace("#THIRD_INVOCATION", patent.third_invocation)
  main = main.replace("#REMAINDER", patent.remainder)
  main = main.replace("#RIGHTS_CLAUSE", patent.rights_clause)
  main = main.replace("#DGR_PLURAL", patent.degree_plural)
  f = open("main.tex", "w")
  f.write(main)
  f.close()

# Continues "make_main" for letters patent of "other" type.
def make_main_other():
  patent = Patent_Other(inputs.ramno, inputs.day, inputs.month, inputs.year,
                        inputs.filling)
  f = open("base_other.tex", "r")
  main = f.read()
  f.close()
  main = main.replace("#RAMNO", str(patent.ramno))
  main = main.replace("#DAY", str(patent.day))
  main = main.replace("#MONTH", patent.month)
  main = main.replace("#YEAR", str(patent.year))
  main = main.replace("#FILLING", patent.filling)
  f = open("main.tex", "w")
  f.write(main)
  f.close()

# Ronseal.
def make_pdf():
  os.system("xelatex main.tex")
  os.system("cp main.pdf out.pdf")
  os.system("rm main.aux main.log main.pdf main.tex")

###################
# RUN AND WRAP UP #
###################

def run():
  make_main()
  make_pdf()
run()
