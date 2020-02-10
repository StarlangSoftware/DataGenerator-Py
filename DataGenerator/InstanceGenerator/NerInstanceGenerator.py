from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from Classification.Instance.Instance import Instance
from Corpus.Sentence import Sentence
from NamedEntityRecognition.NamedEntityType import NamedEntityType

from DataGenerator.InstanceGenerator.SimpleWindowInstanceGenerator import SimpleWindowInstanceGenerator


class NerInstanceGenerator(SimpleWindowInstanceGenerator):

    def addAttributesForWords(self, current: Instance, sentence: Sentence, wordIndex: int):
        pass

    def addAttributesForEmptyWords(self, current: Instance, emptyWord: str):
        pass

    def generateInstanceFromSentence(self, sentence: Sentence, wordIndex: int) -> Instance:
        word = sentence.getWord(wordIndex)
        if isinstance(word, AnnotatedWord):
            classLabel = NamedEntityType.getNamedEntityString(word.getNamedEntityType())
            current = Instance(classLabel)
            self.addAttributes(current, sentence, wordIndex)
            return current
