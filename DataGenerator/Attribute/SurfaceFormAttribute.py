from Classification.Attribute.DiscreteAttribute import DiscreteAttribute


class SurfaceFormAttribute(DiscreteAttribute):

    """
    Discrete attribute for a given word. Returns the surface form.

    PARAMETERS
    ----------
    surfaceForm : str
        Surface form of the word.
    """
    def __init__(self, surfaceForm: str):
        super().__init__(surfaceForm)
