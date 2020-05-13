from distutils.core import setup

setup(
    name='NlpToolkit-DataGenerator',
    version='1.0.2',
    packages=['DataGenerator', 'DataGenerator.Attribute', 'DataGenerator.CorpusGenerator',
              'DataGenerator.DatasetGenerator', 'DataGenerator.InstanceGenerator'],
    url='https://github.com/olcaytaner/DataGenerator-Py',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='Classification dataset generator library for high level Nlp tasks',
    install_requires=['NlpToolkit-AnnotatedSentence', 'NlpToolkit-AnnotatedTree', 'NlpToolkit-Classification',
                      'NlpToolkit-MorphologicalDisambiguation']
)
