from Classification.Attribute.BinaryAttribute import BinaryAttribute
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse


class LastIGContainsPossessiveAttribute(BinaryAttribute):

    def __init__(self, parse: MorphologicalParse):
        """
        Binary attribute for a given word. If the last inflectional group of the word contains POSSESSIVE tag,
        the attribute will be "true", otherwise "false".

        PARAMETERS
        ----------
        parse : MorphologicalParse
            Morphological parse of the word.
        """
        super().__init__(parse.lastIGContainsPossessive())
