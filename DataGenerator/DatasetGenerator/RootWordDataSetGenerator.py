from DataGenerator.DatasetGenerator.DataSetGenerator import DataSetGenerator
from DataGenerator.InstanceGenerator.RootWordInstanceGenerator import RootWordInstanceGenerator


class RootWordDataSetGenerator(DataSetGenerator):

    def __init__(self,
                 folder: str,
                 pattern: str,
                 rootWordInstanceGenerator: RootWordInstanceGenerator):
        """
        Constructor for the RootWordDataSetGenerator which takes input the data directory, the pattern for the training
        files included, and an instanceGenerator. The constructor calls its super class with these inputs.

        PARAMETERS
        ----------
        folder : str
            Directory where the treebank files reside.
        pattern : str
            Pattern of the tree files to be included in the treebank. Use "." for all files.
        rootWordInstanceGenerator : RootWordInstanceGenerator
            The instance generator used to generate the dataset.
        """
        super().__init__(folder, pattern, rootWordInstanceGenerator)
