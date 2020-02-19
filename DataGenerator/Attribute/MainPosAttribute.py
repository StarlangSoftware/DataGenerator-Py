from Classification.Attribute.DiscreteAttribute import DiscreteAttribute
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse


class MainPosAttribute(DiscreteAttribute):

    def __init__(self, parse: MorphologicalParse):
        """
        Discrete attribute for a given word. Returns the last part of speech (main part of speech) of the word

        PARAMETERS
        ----------
        parse : MorphologicalParse
            Morphological parse of the word.
        """
        super().__init__(parse.getPos())
