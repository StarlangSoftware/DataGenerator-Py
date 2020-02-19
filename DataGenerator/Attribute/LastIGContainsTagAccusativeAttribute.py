from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse
from MorphologicalAnalysis.MorphologicalTag import MorphologicalTag

from DataGenerator.Attribute.LastIGContainsTagAttribute import LastIGContainsTagAttribute


class LastIGContainsTagAccusativeAttribute(LastIGContainsTagAttribute):

    def __init__(self, parse: MorphologicalParse):
        """
        Binary attribute for a given word. If the last inflectional group of the word contains ACCUSATIVE tag,
        the attribute will be "true", otherwise "false".

        PARAMETERS
        ----------
        parse : MorphologicalParse
            Morphological parse of the word.
        """
        super().__init__(parse, MorphologicalTag.ACCUSATIVE)
