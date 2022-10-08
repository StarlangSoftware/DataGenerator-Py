from AnnotatedSentence.ViewLayerType import ViewLayerType
from AnnotatedTree.TreeBankDrawable import TreeBankDrawable
from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from DisambiguationCorpus.DisambiguatedWord import DisambiguatedWord
from DisambiguationCorpus.DisambiguationCorpus import DisambiguationCorpus


class TreeDisambiguationCorpusGenerator:

    __tree_bank: TreeBankDrawable

    def __init__(self,
                 folder: str,
                 pattern: str):
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
        self.__tree_bank = TreeBankDrawable(folder, pattern)

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
        for i in range(self.__tree_bank.size()):
            parse_tree = self.__tree_bank.get(i)
            if parse_tree.layerAll(ViewLayerType.INFLECTIONAL_GROUP):
                sentence = parse_tree.generateAnnotatedSentence()
                disambiguation_sentence = AnnotatedSentence()
                for j in range(sentence.wordCount()):
                    annotated_word = sentence.getWord(j)
                    if isinstance(annotated_word, AnnotatedWord):
                        disambiguation_sentence.addWord(DisambiguatedWord(annotated_word.getName(),
                                                                         annotated_word.getParse()))
                corpus.addSentence(disambiguation_sentence)
        return corpus
