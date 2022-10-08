from Classification.Instance.Instance import Instance
from Corpus.Sentence import Sentence

from DataGenerator.InstanceGenerator.InstanceGenerator import InstanceGenerator
from abc import abstractmethod


class SimpleWindowInstanceGenerator(InstanceGenerator):

    @abstractmethod
    def addAttributesForWords(self,
                              current: Instance,
                              sentence: Sentence,
                              wordIndex: int):
        pass

    @abstractmethod
    def addAttributesForEmptyWords(self,
                                   current: Instance,
                                   emptyWord: str):
        pass

    def addAttributes(self,
                      current: Instance,
                      sentence: Sentence,
                      wordIndex: int):
        """
        addAttributes adds all attributes of the previous words, the current wordn, and next words of the given word
        to the given instance. If the previous or next words does not exists, the method calls
        addAttributesForEmptyWords method. If the word does not exists in the dictionary or the required annotation
        layer does not exists in the annotated word, the method throws InstanceNotGenerated. The window size determines
        the number of previous and next words.

        PARAMETERS
        ----------
        current : Instance
            Current classification instance to which attributes will be added.
        sentence : Sentence
            Input sentence.
        wordIndex : int
            The index of the word in the sentence.
        """
        for i in range(self.window_size):
            if wordIndex - self.window_size + i >= 0:
                self.addAttributesForWords(current, sentence, wordIndex - self.window_size + i)
            else:
                self.addAttributesForEmptyWords(current, "<s>")
            self.addAttributesForWords(current, sentence, wordIndex)
        for i in range(self.window_size):
            if wordIndex + i + 1 < sentence.wordCount():
                self.addAttributesForWords(current, sentence, wordIndex + i + 1)
            else:
                self.addAttributesForEmptyWords(current, "</s>")
