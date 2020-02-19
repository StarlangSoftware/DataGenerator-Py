from Classification.Attribute.BinaryAttribute import BinaryAttribute
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse


class IsNumberAttribute(BinaryAttribute):

    def __init__(self, parse: MorphologicalParse):
        """
        Binary attribute for a given word. If the word is represents a number (if the morphological parse contains
        tag REAL or CARDINAL), the attribute will have the value "true", otherwise "false".

        PARAMETERS
        ----------
        parse : MorphologicalParse
            Morphological parse of the word.
        """
        super().__init__(parse.isNumber())
