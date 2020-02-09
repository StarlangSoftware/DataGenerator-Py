from Classification.Attribute.BinaryAttribute import BinaryAttribute
from Dictionary.Word import Word


class IsTimeAttribute(BinaryAttribute):

    """
    Binary attribute for a given word. If the word represents a time form, the attribute will have the
    value "true", otherwise "false".

    PARAMETERS
    ----------
    surfaceForm : str
        Surface form of the word.
    """
    def __init__(self, surfaceForm: str):
        super().__init__(Word.isTime(surfaceForm))
