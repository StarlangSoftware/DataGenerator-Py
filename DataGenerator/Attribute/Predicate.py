from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from Classification.Attribute.DiscreteAttribute import DiscreteAttribute
from Corpus.Sentence import Sentence


class Predicate(DiscreteAttribute):

    def __init__(self,
                 sentence: Sentence,
                 index: int):
        """
        Discrete attribute for a given word. Returns the nearest predicate word to the given word

        PARAMETERS
        ----------
        sentence : Sentence
            Sentence where current word is in.
        index : int
            Position of the current word in the sentence
        """
        if isinstance(sentence, AnnotatedSentence):
            sentence.getPredicate(index)
