from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from AnnotatedSentence.AnnotatedCorpus import AnnotatedCorpus
from MorphologicalDisambiguation.DisambiguatedWord import DisambiguatedWord
from MorphologicalDisambiguation.DisambiguationCorpus import DisambiguationCorpus


class TreeDisambiguationCorpusGenerator:

    __annotatedCorpus: AnnotatedCorpus

    def __init__(self, folder: str, pattern: str):
        """
        Constructor for the DisambiguationCorpusGenerator which takes input the data directory and the pattern for the
        training files included. The constructor loads the corpus from the given directory including the given files
        the given pattern.

        PARAMETERS
        ----------
        folder : str
            Directory where the sentence files reside.
        pattern : str
            Pattern of the tree files to be included in the corpus. Use "." for all files.
        """
        self.__annotatedCorpus = AnnotatedCorpus(folder, pattern)

    def generate(self) -> DisambiguationCorpus:
        """
        Creates a morphological disambiguation corpus from the corpus.

        RETURNS
        -------
        DisambiguationCorpus
            Created disambiguation corpus.
        """
        corpus = DisambiguationCorpus()
        for i in range(self.__annotatedCorpus.sentenceCount()):
            sentence = self.__annotatedCorpus.getSentence(i)
            disambiguationSentence = AnnotatedSentence()
            for j in range(sentence.wordCount()):
                annotatedWord = sentence.getWord(j)
                if isinstance(annotatedWord, AnnotatedWord):
                    disambiguationSentence.addWord(DisambiguatedWord(annotatedWord.getName(),
                                                                     annotatedWord.getParse()))
            corpus.addSentence(disambiguationSentence)
        return corpus
