from Classification.Attribute.BinaryAttribute import BinaryAttribute
from NamedEntityRecognition.Gazetteer import Gazetteer


class IsPersonGazetteer(BinaryAttribute):

    gazetteer = Gazetteer("PERSON", "gazetteer-person.txt")

    """
    Binary attribute for a given word. If the word is listed in the Person Gazetteer file, the attribute will
    have the value "true", otherwise "false".

    PARAMETERS
    ----------
    surfaceForm : str
        Surface form of the word.
    """
    def __init__(self, surfaceForm: str):
        super().__init__(self.gazetteer.contains(surfaceForm))
