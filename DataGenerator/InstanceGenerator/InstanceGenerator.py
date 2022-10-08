from abc import abstractmethod

from Classification.Instance.Instance import Instance
from Corpus.Sentence import Sentence


class InstanceGenerator:

    window_size: int

    @abstractmethod
    def generateInstanceFromSentence(self,
                                     sentence: Sentence,
                                     wordIndex: int) -> Instance:
        pass
