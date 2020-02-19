from Classification.Attribute.DiscreteAttribute import DiscreteAttribute


class SurfaceFormAttribute(DiscreteAttribute):

    def __init__(self, surfaceForm: str):
        """
        Discrete attribute for a given word. Returns the surface form.

        PARAMETERS
        ----------
        surfaceForm : str
            Surface form of the word.
        """
        super().__init__(surfaceForm)
