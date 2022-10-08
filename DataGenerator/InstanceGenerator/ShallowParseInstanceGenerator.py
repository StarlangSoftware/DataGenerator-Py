from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from Classification.Instance.Instance import Instance
from Corpus.Sentence import Sentence

from DataGenerator.InstanceGenerator.SimpleWindowInstanceGenerator import SimpleWindowInstanceGenerator


class ShallowParseInstanceGenerator(SimpleWindowInstanceGenerator):

    def addAttributesForWords(self,
                              current: Instance,
                              sentence: Sentence,
                              wordIndex: int):
        pass

    def addAttributesForEmptyWords(self,
                                   current: Instance,
                                   emptyWord: str):
        pass

    def generateInstanceFromSentence(self,
                                     sentence: Sentence,
                                     wordIndex: int) -> Instance:
        """
        Generates a single classification instance of the Shallow Parse problem for the given word of the given
        sentence. If the  word has not been labeled with shallow parse tag yet, the method returns null.

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
            class_label = word.getShallowParse()
            current = Instance(class_label)
            self.addAttributes(current, sentence, wordIndex)
            return current
