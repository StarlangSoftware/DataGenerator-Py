from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.TreeBankDrawable import TreeBankDrawable
from Classification.DataSet.DataSet import DataSet

from DataGenerator.InstanceGenerator.InstanceGenerator import InstanceGenerator


class DataSetGenerator:

    __treeBank: TreeBankDrawable
    instanceGenerator: InstanceGenerator

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
    def __init__(self, folder: str, pattern: str, instanceGenerator: InstanceGenerator):
        self.__treeBank = TreeBankDrawable(folder, pattern)
        self.instanceGenerator = instanceGenerator

    """
    Mutator for the instanceGenerator attribute.

    PARAMETERS
    ----------
    instanceGenerator : InstanceGenerator
        Input instanceGenerator
    """
    def setInstanceGenerator(self, instanceGenerator: InstanceGenerator):
        self.instanceGenerator = instanceGenerator

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
    def generateInstanceListFromTree(self, parseTree: ParseTreeDrawable) -> list:
        instanceList = []
        annotatedSentence = parseTree.generateAnnotatedSentence()
        for i in range(annotatedSentence.wordCount()):
            generatedSentence = self.instanceGenerator.generateInstanceFromSentence(annotatedSentence, i)
            if generatedSentence is not None:
                instanceList.append(generatedSentence)
        return instanceList

    """
    Creates a dataset from the treeBank. Calls generateInstanceListFromTree for each parse tree in the treebank.

    RETURNS
    -------
    DataSet
        Created dataset.
    """
    def generate(self) -> DataSet:
        dataSet = DataSet()
        for i in range(self.__treeBank.size()):
            parseTree = self.__treeBank.get(i)
            dataSet.addInstanceList(self.generateInstanceListFromTree(parseTree))
        return dataSet
