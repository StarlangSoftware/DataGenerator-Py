from Classification.Attribute.BinaryAttribute import BinaryAttribute
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse


class LastIGContainsPossessiveAttribute(BinaryAttribute):

    """
    Binary attribute for a given word. If the last inflectional group of the word contains POSSESSIVE tag,
    the attribute will be "true", otherwise "false".

    PARAMETERS
    ----------
    parse : MorphologicalParse
        Morphological parse of the word.
    """
    def __init__(self, parse: MorphologicalParse):
        super().__init__(parse.lastIGContainsPossessive())
