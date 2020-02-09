from Classification.Attribute.BinaryAttribute import BinaryAttribute
from NamedEntityRecognition.Gazetteer import Gazetteer


class IsLocationGazetteer(BinaryAttribute):

    gazetteer = Gazetteer("LOCATION", "gazetteer-location.txt")

    """
    Binary attribute for a given word. If the word is listed in the Location Gazetteer file, the attribute will
    have the value "true", otherwise "false".

    PARAMETERS
    ----------
    surfaceForm : str
        Surface form of the word.
    """
    def __init__(self, surfaceForm: str):
        super().__init__(self.gazetteer.contains(surfaceForm))
