ordinals = [None, "first", "second", "third", "fourth", "fifth", "sixth",
            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth",
            "thirteenth", "fourteenth", "fifteenth", "sixteenth",
            "eighteenth", "nineteenth", "twentieth", "twenty-first",
            "twenty-second", "twenty-third", "twenty-fourth",
            "twenty-fifth", "twenty-sixth", "twenty-seventh",
            "twenty-eighth", "twenty-ninth", "thirtieth"]

advance_clauses = dict()
advance_clauses["peer"] = "advance, create and prefer"
advance_clauses["baronet"] = "erect, appoint and create"

trusty_clauses = dict()
trusty_clauses["duke"] = "right trusty and right entirely beloved cousin"
trusty_clauses["marquess"] = "right trusty and entirely beloved cousin"
trusty_clauses["earl"] = trusty_clauses["marquess"]
trusty_clauses["viscount"] = "right trusty and well beloved cousin"
trusty_clauses["baron"] = "trusty and well beloved"

state_clauses = dict()
state_clauses["peer"] = "state, degree, style, dignity, title and honour"
state_clauses["baronet"] = "dignity, state and degree"

dignify_clauses = dict()
dignify_clauses["duke"] = ("and by these presents do dignify, invest and "+
                           "ennoble him by girding him with a sword and "+
                           "putting a cap of honour and a coronet of gold "+
                           "on his head, and by giving into his hand a "+
                           "rod of gold,")
dignify_clauses["marquess"] = dignify_clauses["duke"]
dignify_clauses["earl"] = ("and by these presents do dignify, invest and "+
                           "ennoble him by girding him with a sword and "+
                           "putting a cap of honour and a coronet of gold "+
                           "on his head,")
dignify_clauses["female"] = ("and by these presents do dignify, invest "+
                             "and really ennoble her with such name, "+
                             "state, degree, title and honour of ")

name_clauses = dict()
name_clauses["duke"] = ("the said name, state, degree, style, dignity, "+
                        "title and honour of")
name_clauses["marquess"] = name_clauses["duke"]
name_clauses["earl"] = ("the said name, degree, style, dignity, title and "+
                        "honour of")

pronouns_nominative = dict()
pronouns_nominative["male"] = "he"
pronouns_nominative["female"] = "she"

pronouns_dative = dict()
pronouns_dative["male"] = "him"
pronouns_dative["female"] = "her"

pronouns_possessive = dict()
pronouns_possessive["male"] = "his"
pronouns_possessive["female"] = "her"

rights_clauses = dict()
rights_clauses["peer"] = ("rights, privileges, pre-eminences, immunities "+
                          "and advantages")
rights_clauses["baronet"] = ("rights, privileges, precedences and "+
                             "advantages")

degree_clauses = dict()
degree_clauses["duke"] = "a duke"
degree_clauses["marquess"] = "a marquess"
degree_clauses["earl"] = "an earl"
degree_clauses["viscount"] = "a viscount"
degree_clauses["baron"] = "a baron"
degree_clauses["baronet"] = "a baronet"

degrees_plural = dict()
degrees_plural["duke"] = "dukes"
degrees_plural["marquess"] = "marquess"
degrees_plural["earl"] = "earls"
degrees_plural["viscount"] = "viscounts"
degrees_plural["baron"] = "barons"

standard_remainders = dict()
standard_remainders["heirs-male"] = ("and the heirs male of #POSSESSIVE "+
                                     "body, lawfully begotten and to be "+
                                     "begotten")
standard_remainders["heirs-general"] = ("and the heirs of #POSSESSIVE "+
                                        "body, lawfully begotten and to "+
                                        "be begotten")
standard_remainders["heirs-male-and-bastards"] = ("and the heirs male of "+
                                                  "#POSSESSIVE body")
standard_remainders["heirs-general-and-bastards"] = ("and the heirs of "+
                                                     "#POSSESSIVE body")
standard_remainders["perpetual"] = ("and #POSSESSIVE heirs whatsoever, "+
                                    "or, on the failure of such an heir "+
                                    "to present himself to us, our heirs "+
                                    "and successors, within one year of "+
                                    "his inheritance, to whomsoever we, "+
                                    "our heirs and successors, shall "+
                                    "choose, and his heirs in like "+
                                    "fashion, so that the title may have "+
                                    "perpetual succession")
standard_remainders["life"] = "for #POSSESSIVE life"
