import unittest

from DataGenerator.CorpusGenerator.SentenceDisambiguationCorpusGenerator import SentenceDisambiguationCorpusGenerator


class SentenceDisambiguationCorpusGeneratorTest(unittest.TestCase):

    def test_Generate(self):
        sentenceDisambiguationCorpusGenerator = SentenceDisambiguationCorpusGenerator("../../../sentences/", ".dev")
        disambiguationCorpus = sentenceDisambiguationCorpusGenerator.generate()
        self.assertEquals(10, disambiguationCorpus.sentenceCount())
        self.assertEquals(101, disambiguationCorpus.numberOfWords())
        self.assertEquals(14, disambiguationCorpus.maxSentenceLength())


if __name__ == '__main__':
    unittest.main()
