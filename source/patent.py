"""
This code defines an abstract PATENT class, to be inherited by child classes.
"""

# Standard imports.
import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar

# Local imports.
from .constants import ORDINALS

# Local constants.
WORKING_STEM = "main"
DEFAULT_PATH_TO_OUTPUT = "out.pdf"
PATH_OBJ_TO_IMAGE_DIR = Path(__file__).parent/"images"

##############
# MAIN CLASS #
##############

@dataclass
class Patent:
    """ The class in question. """
    # Class attributes.
    LATEX_COMMAND: ClassVar[str] = "xelatex"
    WORKING_FN: ClassVar[str] = WORKING_STEM+".tex"
    IMMEDIATE_OUTPUT_FN: ClassVar[str] = WORKING_STEM+".pdf"
    EXTENSIONS_TO_REMOVE: ClassVar[tuple] = (".aux", ".log", ".pdf", ".tex")
    PATH_TO_BASE: ClassVar[str] = str(Path(__file__).parent/"tex"/"base.tex")
    PATH_TO_TOP_IMAGE: ClassVar[str] = \
        str(PATH_OBJ_TO_IMAGE_DIR/"thomas_hosker_duke_of.png")
    PATH_TO_SIGNATURE: ClassVar[str] = \
        str(PATH_OBJ_TO_IMAGE_DIR/"signature.png")
    PATH_TO_SEAL: ClassVar[str] = str(PATH_OBJ_TO_IMAGE_DIR/"seal.png")
    TOP_IMAGE_MARKER: ClassVar[str] = "#TOP_IMAGE"
    SIGNATURE_MARKER: ClassVar[str] = "#SIGNATURE"
    SEAL_MARKER: ClassVar[str] = "#SEAL"
    RAMNO_MARKER: ClassVar[str] = "#RAMNO"
    DAY_ORDSTR_MARKER: ClassVar[str] = "#DAY_ORDSTR"
    MONTH_STR_MARKER: ClassVar[str] = "#MONTH_STR"
    YEAR_ORDSTR_MARKER: ClassVar[str] = "#YEAR_ORDSTR"
    BODY_MARKER: ClassVar[str] = "#BODY"

    # Object attributes.
    ramno: int = None
    day_num: int = None
    day_ordstr: str = None
    month_num: int = None
    month_str: str = None
    year_num: int = None
    year_ordstr: str = None
    body: str = None
    path_to_output: str = DEFAULT_PATH_TO_OUTPUT
    clean_bool: bool = True

    def __post_init__(self):
        self.update_date_fields()

    def update_date_fields(self):
        """ Set any unset date fields, where possible. """
        if self.day_num and not self.day_ordstr:
            self.day_ordstr = ORDINALS[self.day_num]
        if (self.month_num is not None) and (not self.month_str):
            self.month_str = ORDINALS[self.month_num]
        if self.year_num and not self.year_ordstr:
            self.year_ordstr = ORDINALS[self.year_num]

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
            (self.BODY_MARKER, self.body)
        )
        for pair in replacement_pairs:
            tex_str = tex_str.replace(pair[0], pair[1])
        with open(self.WORKING_FN, "w") as working_tex:
            working_tex.write(tex_str)

    def compile_working_tex(self):
        """ Compile the working TeX file. """
        subprocess.run([self.LATEX_COMMAND, self.WORKING_FN], check=True)
        shutil.copyfile(self.IMMEDIATE_OUTPUT_FN, self.path_to_output)

    def clean(self):
        """ Clean up any redundant generated files. """
        for extension in self.EXTENSIONS_TO_REMOVE:
            os.remove(WORKING_STEM+extension)

    def generate(self):
        """ (1) Build the TeX file. (2) Compile it. (3) Clean (if req). """
        self.build_working_tex()
        self.compile_working_tex()
        if self.clean_bool:
            self.clean()
