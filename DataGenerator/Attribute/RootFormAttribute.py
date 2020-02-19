from Classification.Attribute.DiscreteAttribute import DiscreteAttribute
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse


class RootFormAttribute(DiscreteAttribute):

    def __init__(self, parse: MorphologicalParse):
        """
        Discrete attribute for a given word. Returns the the root word

        PARAMETERS
        ----------
        parse : MorphologicalParse
            Morphological parse of the word.
        """
        super().__init__(parse.getWord().getName())
