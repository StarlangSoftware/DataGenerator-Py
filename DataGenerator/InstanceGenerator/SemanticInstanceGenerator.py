from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from Classification.Instance.CompositeInstance import CompositeInstance
from Classification.Instance.Instance import Instance
from Corpus.Sentence import Sentence
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from WordNet.WordNet import WordNet

from DataGenerator.InstanceGenerator.SimpleWindowInstanceGenerator import SimpleWindowInstanceGenerator


class SemanticInstanceGenerator(SimpleWindowInstanceGenerator):

    __fsm: FsmMorphologicalAnalyzer
    __wordNet: WordNet

    def __init__(self, fsm: FsmMorphologicalAnalyzer, wordNet: WordNet):
        """
        Constructor for the semantic instance generator. Takes morphological analyzer and wordnet as input to set the
        corresponding variables.

        PARAMETERS
        ----------
        fsm : FsmMorphologicalAnalyzer
            Morphological analyzer to be used.
        wordNet : WordNet
            Wordnet to be used.
        """
        self.__fsm = fsm
        self.__wordNet = wordNet

    def addAttributesForWords(self, current: Instance, sentence: Sentence, wordIndex: int):
        """
        Generates a single classification instance of the WSD problem for the given word of the given sentence. If the
        word has not been labeled with sense tag yet, the method returns null. In the WSD problem, the system also
        generates and stores all possible sense labels for the current instance. In this case, a classification
        instance will not have all labels in the dataset, but some subset of it.

        PARAMETERS
        ----------
        sentence : Sentence
            Input sentence.
        wordIndex : int
            The index of the word in the sentence.

        RETURNS
        -------
        Instance
            Classification instance.
        """
        pass

    def addAttributesForEmptyWords(self, current: Instance, emptyWord: str):
        pass

    def generateInstanceFromSentence(self, sentence: Sentence, wordIndex: int) -> Instance:
        if isinstance(sentence, AnnotatedSentence):
            possibleSynSets = sentence.constructSynSets(self.__wordNet, self.__fsm, wordIndex)
            word = sentence.getWord(wordIndex)
            if isinstance(word, AnnotatedWord):
                classLabel = word.getSemantic()
                current = CompositeInstance(classLabel)
                possibleClassLabels = []
                for synSet in possibleSynSets:
                    possibleClassLabels.append(synSet.getId())
                current.setPossibleClassLabels(possibleClassLabels)
                self.addAttributes(current, sentence, wordIndex)
                return current
