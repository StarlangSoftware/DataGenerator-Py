from Classification.Attribute.BinaryAttribute import BinaryAttribute
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse


class IsProperNounAttribute(BinaryAttribute):

    def __init__(self, parse: MorphologicalParse):
        """
        Binary attribute for a given word. If the word represents a date (if the morphological parse contains
        tag PROPERNOUN), the attribute will have the value "true", otherwise "false".

        PARAMETERS
        ----------
        parse : MorphologicalParse
            Morphological parse of the word.
        """
        super().__init__(parse.isProperNoun())
