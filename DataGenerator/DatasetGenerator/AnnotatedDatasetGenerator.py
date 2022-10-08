from AnnotatedSentence.AnnotatedCorpus import AnnotatedCorpus
from Classification.DataSet.DataSet import DataSet

from DataGenerator.InstanceGenerator.InstanceGenerator import InstanceGenerator


class AnnotatedDatasetGenerator:

    __corpus: AnnotatedCorpus
    __instance_generator: InstanceGenerator

    def __init__(self,
                 folder: str,
                 pattern: str,
                 instanceGenerator: InstanceGenerator):
        """
        Constructor for the AnnotatedDataSetGenerator which takes input the data directory, the pattern for the
        training files included, and an instanceGenerator. The constructor loads the sentence corpus from the given
        directory including the given files having the given pattern.

        PARAMETERS
        ----------
        folder : str
            Directory where the corpus files reside.
        pattern : str
            Pattern of the tree files to be included in the treebank. Use "." for all files.
        instanceGenerator : InstanceGenerator
            The instance generator used to generate the dataset.
        """
        self.__corpus = AnnotatedCorpus(folder, pattern)
        self.__instance_generator = instanceGenerator

    def setInstanceGenerator(self, instanceGenerator: InstanceGenerator):
        """
        Mutator for the instanceGenerator attribute.

        PARAMETERS
        ----------
        instanceGenerator : InstanceGenerator
            Input instanceGenerator
        """
        self.__instance_generator = instanceGenerator

    def generate(self) -> DataSet:
        """
        Creates a dataset from the corpus. Calls generateInstanceFromSentence for each parse sentence in the corpus.

        RETURNS
        -------
        DataSet
            Created dataset.
        """
        data_set = DataSet()
        for sentence in self.__corpus.sentences:
            for j in range(sentence.wordCount()):
                generated_instance = self.__instance_generator.generateInstanceFromSentence(sentence, j)
                if generated_instance is not None:
                    data_set.addInstance(generated_instance)
        return data_set
