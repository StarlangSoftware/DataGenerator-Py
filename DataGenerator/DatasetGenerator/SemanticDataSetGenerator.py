from DataGenerator.DatasetGenerator.DataSetGenerator import DataSetGenerator
from DataGenerator.InstanceGenerator.SemanticInstanceGenerator import SemanticInstanceGenerator


class SemanticDataSetGenerator(DataSetGenerator):

    def __init__(self,
                 folder: str,
                 pattern: str,
                 semanticInstanceGenerator: SemanticInstanceGenerator):
        """
        Constructor for the NerDataSetGenerator which takes input the data directory, the pattern for the training files
        included, and an instanceGenerator. The constructor calls its super class with these inputs.

        PARAMETERS
        ----------
        folder : str
            Directory where the treebank files reside.
        pattern : str
            Pattern of the tree files to be included in the treebank. Use "." for all files.
        semanticInstanceGenerator : SemanticInstanceGenerator
            The instance generator used to generate the dataset.
        """
        super().__init__(folder, pattern, semanticInstanceGenerator)
