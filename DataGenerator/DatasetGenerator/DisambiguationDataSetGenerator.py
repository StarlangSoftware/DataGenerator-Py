from DataGenerator.DatasetGenerator.DataSetGenerator import DataSetGenerator
from DataGenerator.InstanceGenerator.DisambiguationInstanceGenerator import DisambiguationInstanceGenerator


class DisambiguationDataSetGenerator(DataSetGenerator):

    """
    Constructor for the DisambiguationDataSetGenerator which takes input the data directory, the pattern for the training files
    included, and an instanceGenerator. The constructor calls its super class with these inputs.

    PARAMETERS
    ----------
    folder : str
        Directory where the treebank files reside.
    pattern : str
        Pattern of the tree files to be included in the treebank. Use "." for all files.
    disambiguationInstanceGenerator : DisambiguationInstanceGenerator
        The instance generator used to generate the dataset.
    """
    def __init__(self, folder: str, pattern: str, disambiguationInstanceGenerator: DisambiguationInstanceGenerator):
        super().__init__(folder, pattern, disambiguationInstanceGenerator)
