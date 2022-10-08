import unittest

from DataGenerator.CorpusGenerator.TreeDisambiguationCorpusGenerator import TreeDisambiguationCorpusGenerator


class TreeDisambiguationCorpusGeneratorTest(unittest.TestCase):

    def test_Generate(self):
        treeDisambiguationCorpusGenerator = TreeDisambiguationCorpusGenerator("../../../trees/", ".dev")
        disambiguationCorpus = treeDisambiguationCorpusGenerator.generate()
        self.assertEqual(10, disambiguationCorpus.sentenceCount())
        self.assertEqual(88, disambiguationCorpus.numberOfWords())
        self.assertEqual(13, disambiguationCorpus.maxSentenceLength())


if __name__ == '__main__':
    unittest.main()
