from AnnotatedSentence.ViewLayerType import ViewLayerType
from AnnotatedTree.TreeBankDrawable import TreeBankDrawable
from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from MorphologicalDisambiguation.DisambiguatedWord import DisambiguatedWord
from MorphologicalDisambiguation.DisambiguationCorpus import DisambiguationCorpus


class TreeDisambiguationCorpusGenerator:

    __treeBank: TreeBankDrawable

    def __init__(self, folder: str, pattern: str):
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
        self.__treeBank = TreeBankDrawable(folder, pattern)

    def generate(self) -> DisambiguationCorpus:
        """
        Creates a morphological disambiguation corpus from the treeBank. Calls generateAnnotatedSentence for each parse
        tree in the treebank.

        RETURNS
        -------
        DisambiguationCorpus
            Created disambiguation corpus.
        """
        corpus = DisambiguationCorpus()
        for i in range(self.__treeBank.size()):
            parseTree = self.__treeBank.get(i)
            if parseTree.layerAll(ViewLayerType.INFLECTIONAL_GROUP):
                sentence = parseTree.generateAnnotatedSentence()
                disambiguationSentence = AnnotatedSentence()
                for j in range(sentence.wordCount()):
                    annotatedWord = sentence.getWord(j)
                    if isinstance(annotatedWord, AnnotatedWord):
                        disambiguationSentence.addWord(DisambiguatedWord(annotatedWord.getName(),
                                                                         annotatedWord.getParse()))
                corpus.addSentence(disambiguationSentence)
        return corpus
