from Classification.Attribute.BinaryAttribute import BinaryAttribute
from Dictionary.Word import Word


class IsMoneyAttribute(BinaryAttribute):

    def __init__(self, surfaceForm: str):
        """
        Binary attribute for a given word. If the word is "dolar", "euro", "sterlin", etc., the attribute will have the
        value "true", otherwise "false".

        PARAMETERS
        ----------
        surfaceForm : str
            Surface form of the word.
        """
        super().__init__(Word.isMoney(surfaceForm))
