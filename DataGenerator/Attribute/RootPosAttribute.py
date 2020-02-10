from Classification.Attribute.DiscreteAttribute import DiscreteAttribute
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse


class RootPosAttribute(DiscreteAttribute):

    """
    Discrete attribute for a given word. Returns the part of speech of the root word

    PARAMETERS
    ----------
    parse : MorphologicalParse
        Morphological parse of the word.
    """
    def __init__(self, parse: MorphologicalParse):
        super().__init__(parse.getRootPos())
