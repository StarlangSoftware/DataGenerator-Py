from Classification.Attribute.BinaryAttribute import BinaryAttribute
from Dictionary.Word import Word


class IsOrganizationAttribute(BinaryAttribute):

    def __init__(self, surfaceForm: str):
        """
        Binary attribute for a given word. If the word is "corp.", "inc." or "co.", the attribute will have the
        value "true", otherwise "false".

        PARAMETERS
        ----------
        surfaceForm : str
            Surface form of the word.
        """
        super().__init__(Word.isOrganization(surfaceForm))
