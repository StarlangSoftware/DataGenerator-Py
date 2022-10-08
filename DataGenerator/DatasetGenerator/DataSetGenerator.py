from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.TreeBankDrawable import TreeBankDrawable
from Classification.DataSet.DataSet import DataSet

from DataGenerator.InstanceGenerator.InstanceGenerator import InstanceGenerator


class DataSetGenerator:

    __tree_bank: TreeBankDrawable
    __instance_generator: InstanceGenerator

    def __init__(self,
                 folder: str,
                 pattern: str,
                 instanceGenerator: InstanceGenerator):
        """
        Constructor for the DataSetGenerator which takes input the data directory, the pattern for the training files
        included, and an instanceGenerator. The constructor loads the treebank from the given directory
        including the given files having the given pattern. If punctuations are not included, they are removed from
        the data.

        PARAMETERS
        ----------
        folder : str
            Directory where the treebank files reside.
        pattern : str
            Pattern of the tree files to be included in the treebank. Use "." for all files.
        instanceGenerator : InstanceGenerator
            The instance generator used to generate the dataset.
        """
        self.__tree_bank = TreeBankDrawable(folder, pattern)
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

    def generateInstanceListFromTree(self, parseTree: ParseTreeDrawable) -> list:
        """
        The method generates a set of instances (an instance from each word in the tree) from a single tree. The method
        calls the instanceGenerator for each word in the sentence.

        PARAMETERS
        ----------
        parseTree : ParseTreeDrawable
            Parsetree for which a set of instances will be created

        RETURNS
        -------
        list
            A list of instances.
        """
        instance_list = []
        annotated_sentence = parseTree.generateAnnotatedSentence()
        for i in range(annotated_sentence.wordCount()):
            generated_sentence = self.__instance_generator.generateInstanceFromSentence(annotated_sentence, i)
            if generated_sentence is not None:
                instance_list.append(generated_sentence)
        return instance_list

    def generate(self) -> DataSet:
        """
        Creates a dataset from the treeBank. Calls generateInstanceListFromTree for each parse tree in the treebank.

        RETURNS
        -------
        DataSet
            Created dataset.
        """
        data_set = DataSet()
        for i in range(self.__tree_bank.size()):
            parse_tree = self.__tree_bank.get(i)
            data_set.addInstanceList(self.generateInstanceListFromTree(parse_tree))
        return data_set
