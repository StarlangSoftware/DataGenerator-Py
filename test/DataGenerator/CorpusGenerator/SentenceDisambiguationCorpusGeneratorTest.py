import unittest

from DataGenerator.CorpusGenerator.SentenceDisambiguationCorpusGenerator import SentenceDisambiguationCorpusGenerator


class SentenceDisambiguationCorpusGeneratorTest(unittest.TestCase):

    def test_Generate(self):
        sentenceDisambiguationCorpusGenerator = SentenceDisambiguationCorpusGenerator("../../../sentences/", ".dev")
        disambiguationCorpus = sentenceDisambiguationCorpusGenerator.generate()
        self.assertEqual(10, disambiguationCorpus.sentenceCount())
        self.assertEqual(101, disambiguationCorpus.numberOfWords())
        self.assertEqual(14, disambiguationCorpus.maxSentenceLength())


if __name__ == '__main__':
    unittest.main()
