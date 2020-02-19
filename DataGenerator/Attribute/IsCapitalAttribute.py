from Classification.Attribute.BinaryAttribute import BinaryAttribute


class IsCapitalAttribute(BinaryAttribute):

    def __init__(self, surfaceForm: str):
        """
        Binary attribute for a given word. If the starting letter of the word is capital, the attribute will have
        the value "true", otherwise "false".

        PARAMETERS
        ----------
        surfaceForm: str
            Surface form of the word.
        """
        super().__init__(surfaceForm[0:0].isupper())
