from Classification.Attribute.BinaryAttribute import BinaryAttribute
from Dictionary.Word import Word


class IsMoneyAttribute(BinaryAttribute):

    """
    Binary attribute for a given word. If the word is "dolar", "euro", "sterlin", etc., the attribute will have the
    value "true", otherwise "false".

    PARAMETERS
    ----------
    surfaceForm : str
        Surface form of the word.
    """
    def __init__(self, surfaceForm: str):
        super().__init__(Word.isMoney(surfaceForm))
