"""
This code holds a class which models the letters patent pertaining to a given
peerage.
"""

# Standard imports.
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar

# Local imports.
from .patent import Patent

# Local constants.
MALE = "male"
FEMALE = "female"
DUKE = "duke"
MARQUESS = "marquess"
EARL = "earl"
VISCOUNT = "viscount"
BARON = "baron"
BARONET = "baronet"
PEERAGE_RANKS = (BARON, VISCOUNT, EARL, MARQUESS, DUKE)

##############
# MAIN CLASS #
##############

@dataclass
class PatentPeerage(Patent):
    """ The class in question. """
    # Class variables.
    PATH_TO_BASE: ClassVar[str] = \
        str(Path(__file__).parent/"tex"/"base_peerage.tex")
    ADVANCE_CLAUSES: ClassVar[dict] = {
        **dict.fromkeys(PEERAGE_RANKS, "advance, create and prefer"),
        BARONET: "erect, appoint and create"
    }
    TRUSTY_CLAUSES: ClassVar[dict] = {
        DUKE: "right trusty and right entirely beloved cousin",
        MARQUESS: "right trusty and entirely beloved cousin",
        EARL: "right trusty and entirely beloved cousin",
        VISCOUNT: "right trusty and well beloved cousin",
        BARON: "trusty and well beloved",
        BARONET: ""
    }
    STATE_CLAUSES: ClassVar[dict] = {
        **dict.fromkeys(
            PEERAGE_RANKS, "state, degree, style, dignity, title and honour"
        ),
        BARONET: "dignity, state and degree"
    }
    DIGNIFY_CLAUSES: ClassVar[dict] = {
        DUKE: (
            "and by these presents do dignify, invest and ennoble him by "+
            "girding him with a sword and putting a cap of honour and a "+
            "coronet of gold on his head, and by giving into his hand a rod "+
            "of gold,"
        ),
        MARQUESS: (
            "and by these presents do dignify, invest and ennoble him by "+
            "girding him with a sword and putting a cap of honour and a "+
            "coronet of gold on his head, and by giving into his hand a rod "+
            "of gold,"
        ),
        EARL: (
            "and by these presents do dignify, invest and ennoble him by "+
            "girding him with a sword and putting a cap of honour and a "+
            "coronet of gold on his head,"
        ),
        FEMALE: (
            "and by these presents do dignify, invest and really ennoble her "+
            "with such name, state, degree, title and honour of "
        )
    }
    NAME_CLAUSES: ClassVar[dict] = {
        DUKE: (
            "the said name, state, degree, style, dignity, title and honour of"
        ),
        MARQUESS: (
            "the said name, state, degree, style, dignity, title and honour of"
        ),
        EARL: "the said name, degree, style, dignity, title and honour of"
    }
    PRONOUNS_NOMINATIVE: ClassVar[dict] = { MALE: "he", FEMALE: "she" }
    PRONOUNS_DATIVE: ClassVar[dict] = { MALE: "him", FEMALE: "her" }
    PRONOUNS_POSSESSIVE: ClassVar[dict] = { MALE: "his", FEMALE: "her" }
    RIGHTS_CLAUSES: ClassVar[dict] = {
        **dict.fromkeys(
            PEERAGE_RANKS,
            "rights, privileges, pre-eminences, immunities and advantages"
        ),
        BARONET: "rights, privileges, precedences and advantages"
    }
    DEGREE_CLAUSES: ClassVar[dict] = {
        DUKE: "a "+DUKE,
        MARQUESS: "a "+MARQUESS,
        EARL: "an "+EARL,
        VISCOUNT: "a "+VISCOUNT,
        BARON: "a "+BARON,
        BARONET: "a "+BARONET
    }
    DEGREES_PLURAL: ClassVar[dict] = {
        DUKE: DUKE+"s",
        MARQUESS: MARQUESS+"es",
        EARL: EARL+"s",
        VISCOUNT: VISCOUNT+"s",
        BARON: BARON+"s",
        BARONET: BARONET+"s"
    }
    STANDARD_REMAINDERS: ClassVar[dict] = {
        "heirs-male": (
            "and the heirs male of #POSSESSIVE body, lawfully begotten and "+
            "to be begotten"
        ),
        "heirs-general": (
            "and the heirs of #POSSESSIVE body, lawfully begotten and to be "+
            "begotten"
        ),
        "heirs-male-and-bastards": "and the heirs male of #POSSESSIVE body",
        "heirs-general-and-bastards": "and the heirs of #POSSESSIVE body",
        "perpetual": (
            "and #POSSESSIVE heirs whatsoever, or, on the failure of such an "+
            "heir to present himself to us, our heirs and successors, within "+
            "one year of his inheritance, to whomsoever we, our heirs and "+
            "onesuccessors, shall choose, and his heirs in like fashion, so "+
            "that the title may have perpetual succession"
        ),
        "life": "for #POSSESSIVE life"
    }
    GRANTEE_MARKER: ClassVar[str] = "#GRANTEE"
    TITLE_MARKER: ClassVar[str] = "#TITLE"
    SUBSIDIARY_TITLES_MARKER: ClassVar[str] = "#SUBSIDIARY_TITLES"
    WHEREAS_MARKER: ClassVar[str] = "#WHEREAS"
    PRONOUN_NOMINATIVE_MARKER: ClassVar[str] = "#PRONOUN_NOMINATIVE"
    PRONOUN_DATIVE_MARKER: ClassVar[str] = "#PRONOUN_DATIVE"
    PRONOUN_POSSESSIVE_MARKER: ClassVar[str] = "#PRONOUN_POSSESSIVE"
    ADVANCE_CLAUSE_MARKER: ClassVar[str] = "#ADVANCE_CLAUSE"
    TRUSTY_CLAUSE_MARKER: ClassVar[str] = "#TRUSTY_CLAUSE"
    STATE_CLAUSE_MARKER: ClassVar[str] = "#STATE_CLAUSE"
    DIGNIFY_CLAUSE_MARKER: ClassVar[str] = "#DIGNIFY_CLAUSE"
    THIRD_INVOCATION_MARKER: ClassVar[str] = "#THIRD_INVOCATION"
    REMAINDER_MARKER: ClassVar[str] = "#REMAINDER"
    RIGHTS_CLAUSE_MARKER: ClassVar[str] = "#RIGHTS_CLAUSE"
    DEGREE_CLAUSE_MARKER: ClassVar[str] = "#DEGREE_CLAUSE"
    DEGREE_PLURAL_MARKER: ClassVar[str] = "#DEGREE_PLURAL"

    # Fields.
    grantee: str = None
    gender: str = None
    degree: str = None
    title: str = None
    subsidiary_titles: list = None
    subsidiary_titles_str: str = None
    whereas: str = None
    pronoun_nominative: str = None
    pronoun_dative: str = None
    pronoun_possessive: str = None
    advance_clause: str = None
    trusty_clause: str = None
    dignify_clause: str = None
    third_invocation: str = None
    remainder: str = None
    rights_clause: str = None
    degree_clause: str = None
    degree_plural: str = None

    def __post_init__(self):
        super().__post_init__()
        self.subsidiary_titles_str = self.get_subsidiary_titles_str()
        self.whereas = self.get_whereas()
        self.pronoun_nominative = self.PRONOUNS_NOMINATIVE[self.gender]
        self.pronoun_dative = self.PRONOUNS_DATIVE[self.gender]
        self.pronoun_possessive = self.PRONOUNS_POSSESSIVE[self.gender]
        self.advance_clause = self.ADVANCE_CLAUSES[self.degree]
        self.trusty_clause = self.TRUSTY_CLAUSES[self.degree]
        self.state_clause = self.STATE_CLAUSES[self.degree]
        self.dignify_clause = self.get_dignify_clause()
        self.third_invocation = self.get_third_invocation()
        self.remainder = self.get_remainder()
        self.rights_clause = self.RIGHTS_CLAUSES[self.degree]
        self.degree_clause = self.DEGREE_CLAUSES[self.degree]
        self.degree_plural = self.DEGREES_PLURAL[self.degree]

    def get_whereas(self):
        """ Add an hspace, if necessary. """
        result = self.whereas
        if result:
            result = "\\hspace{20pt} "+result
            return result
        return ""

    def get_subsidiary_titles_str(self):
        """ Change the list into an injectable string. """
        if self.subsidiary_titles:
            result = ", ".join(self.subsidiary_titles)
            return result
        return ""

    def get_dignify_clause(self):
        """ Looks up the result. """
        result = ""
        if self.degree in self.DIGNIFY_CLAUSES:
            if self.gender == FEMALE:
                result = self.DIGNIFY_CLAUSES[FEMALE]+self.title+", "
            else:
                result = self.DIGNIFY_CLAUSES[self.degree]
        return result

    def get_third_invocation(self):
        """ Construct the third invocation of the title granted. """
        result = ""
        if self.degree in self.NAME_CLAUSES:
            result = self.NAME_CLAUSES[self.degree]
        return result

    def get_remainder(self):
        """ Look up the result, if appropriate. """
        result = self.remainder
        if self.remainder in self.STANDARD_REMAINDERS:
            result = self.STANDARD_REMAINDERS[self.remainder]
        result = result.replace("#POSSESSIVE", self.pronoun_possessive)
        return result

    def build_working_tex(self):
        """ Build the working TeX file, which we'll then compile. """
        with open(self.PATH_TO_BASE, "r") as base_file:
            tex_str = base_file.read()
        replacement_pairs = (
            (self.TOP_IMAGE_MARKER, self.PATH_TO_TOP_IMAGE),
            (self.SIGNATURE_MARKER, self.PATH_TO_SIGNATURE),
            (self.SEAL_MARKER, self.PATH_TO_SEAL),
            (self.RAMNO_MARKER, str(self.ramno)),
            (self.DAY_ORDSTR_MARKER, self.day_ordstr),
            (self.MONTH_STR_MARKER, self.month_str),
            (self.YEAR_ORDSTR_MARKER, self.year_ordstr),
            (self.GRANTEE_MARKER, self.grantee),
            (self.TITLE_MARKER, self.title),
            (self.SUBSIDIARY_TITLES_MARKER, self.subsidiary_titles_str),
            (self.WHEREAS_MARKER, self.whereas),
            (self.PRONOUN_NOMINATIVE_MARKER, self.pronoun_nominative),
            (self.PRONOUN_DATIVE_MARKER, self.pronoun_dative),
            (self.PRONOUN_POSSESSIVE_MARKER, self.pronoun_possessive),
            (self.ADVANCE_CLAUSE_MARKER, self.advance_clause),
            (self.TRUSTY_CLAUSE_MARKER, self.trusty_clause),
            (self.STATE_CLAUSE_MARKER, self.state_clause),
            (self.DIGNIFY_CLAUSE_MARKER, self.dignify_clause),
            (self.THIRD_INVOCATION_MARKER, self.third_invocation),
            (self.REMAINDER_MARKER, self.remainder),
            (self.RIGHTS_CLAUSE_MARKER, self.rights_clause),
            (self.DEGREE_CLAUSE_MARKER, self.degree_clause),
            (self.DEGREE_PLURAL_MARKER, self.degree_plural)
        )
        for pair in replacement_pairs:
            tex_str = tex_str.replace(pair[0], pair[1])
        with open(self.WORKING_FN, "w") as working_tex:
            working_tex.write(tex_str)
