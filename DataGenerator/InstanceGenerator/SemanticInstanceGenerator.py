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
    __word_net: WordNet

    def __init__(self,
                 fsm: FsmMorphologicalAnalyzer,
                 wordNet: WordNet):
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
        self.__word_net = wordNet

    def addAttributesForWords(self,
                              current: Instance,
                              sentence: Sentence,
                              wordIndex: int):
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

    def addAttributesForEmptyWords(self,
                                   current: Instance,
                                   emptyWord: str):
        pass

    def generateInstanceFromSentence(self,
                                     sentence: Sentence,
                                     wordIndex: int) -> Instance:
        if isinstance(sentence, AnnotatedSentence):
            possible_syn_sets = sentence.constructSynSets(self.__word_net, self.__fsm, wordIndex)
            word = sentence.getWord(wordIndex)
            if isinstance(word, AnnotatedWord):
                class_label = word.getSemantic()
                current = CompositeInstance(class_label)
                possible_class_labels = []
                for synSet in possible_syn_sets:
                    possible_class_labels.append(synSet.getId())
                current.setPossibleClassLabels(possible_class_labels)
                self.addAttributes(current, sentence, wordIndex)
                return current
