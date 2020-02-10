from AnnotatedSentence.ViewLayerType import ViewLayerType
from AnnotatedTree.TreeBankDrawable import TreeBankDrawable
from MorphologicalDisambiguation.DisambiguationCorpus import DisambiguationCorpus


class DisambiguationCorpusGenerator:

    __treeBank: TreeBankDrawable

    """
    Constructor for the DisambiguationCorpusGenerator which takes input the data directory and the pattern for the
    training files included. The constructor loads the treebank from the given directory including the given files
    the given pattern.

    PARAMETERS
    ----------
    folder : str
        Directory where the treebank files reside.
    pattern : str
        Pattern of the tree files to be included in the treebank. Use "." for all files.
    """
    def __init__(self, folder: str, pattern: str):
        self.__treeBank = TreeBankDrawable(folder, pattern)

    """
    Creates a morphological disambiguation corpus from the treeBank. Calls generateAnnotatedSentence for each parse
    tree in the treebank.

    RETURNS
    -------
    DisambiguationCorpus
        Created disambiguation corpus.
    """
    def generate(self) -> DisambiguationCorpus:
        corpus = DisambiguationCorpus()
        for i in range(self.__treeBank.size()):
            parseTree = self.__treeBank.get(i)
            if parseTree.layerAll(ViewLayerType.INFLECTIONAL_GROUP):
                sentence = parseTree.generateAnnotatedSentence()
                corpus.addSentence(sentence)
        return corpus
