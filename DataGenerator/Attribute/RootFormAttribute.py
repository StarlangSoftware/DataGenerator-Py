from Classification.Attribute.DiscreteAttribute import DiscreteAttribute
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse


class RootFormAttribute(DiscreteAttribute):

    """
    Discrete attribute for a given word. Returns the the root word

    PARAMETERS
    ----------
    parse : MorphologicalParse
        Morphological parse of the word.
    """
    def __init__(self, parse: MorphologicalParse):
        super().__init__(parse.getWord().getName())
