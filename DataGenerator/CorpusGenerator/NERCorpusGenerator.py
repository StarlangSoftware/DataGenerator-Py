from AnnotatedSentence.ViewLayerType import ViewLayerType
from AnnotatedTree.TreeBankDrawable import TreeBankDrawable
from NamedEntityRecognition.NERCorpus import NERCorpus


class NERCorpusGenerator:

    __tree_bank: TreeBankDrawable

    def __init__(self,
                 folder: str,
                 pattern: str):
        """
        Constructor for the NERCorpusGenerator which takes input the data directory and the pattern for the
        training files included. The constructor loads the treebank from the given directory including the given files
        the given pattern.

        PARAMETERS
        ----------
        folder : str
            Directory where the treebank files reside.
        pattern : str
            Pattern of the tree files to be included in the treebank. Use "." for all files.
        """
        self.__tree_bank = TreeBankDrawable(folder, pattern)

    def generate(self) -> NERCorpus:
        """
        Creates a morphological disambiguation corpus from the treeBank. Calls generateAnnotatedSentence for each parse
        tree in the treebank.

        RETURNS
        -------
        DisambiguationCorpus
            Created disambiguation corpus.
        """
        corpus = NERCorpus()
        for i in range(self.__tree_bank.size()):
            parseTree = self.__tree_bank.get(i)
            if parseTree.layerAll(ViewLayerType.NER):
                sentence = parseTree.generateAnnotatedSentence()
                corpus.addSentence(sentence)
        return corpus
