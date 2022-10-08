from abc import abstractmethod

from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from Classification.Instance.Instance import Instance
from Corpus.Sentence import Sentence

from DataGenerator.InstanceGenerator.InstanceGenerator import InstanceGenerator


class RootWordInstanceGenerator(InstanceGenerator):

    @abstractmethod
    def addAttributesForPreviousWords(self,
                                      current: Instance,
                                      sentence: Sentence,
                                      wordIndex: int):
        pass

    @abstractmethod
    def addAttributesForEmptyWords(self,
                                   current: Instance,
                                   emptyWord: str):
        pass

    def generateInstanceFromSentence(self,
                                     sentence: Sentence,
                                     wordIndex: int) -> Instance:
        """
        Generates a single classification instance of the root word detection problem for the given word of the
        given sentence. If the word does not have a morphological parse, the method throws InstanceNotGenerated.

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
        word = sentence.getWord(wordIndex)
        if isinstance(word, AnnotatedWord):
            current = Instance(word.getParse().getWord().getName())
            for i in range(self.window_size):
                if wordIndex - self.window_size + i >= 0:
                    self.addAttributesForPreviousWords(current, sentence, wordIndex - self.window_size + i)
                else:
                    self.addAttributesForEmptyWords(current, "<s>")
            self.addAttributesForPreviousWords(current, sentence, wordIndex)
            return current
