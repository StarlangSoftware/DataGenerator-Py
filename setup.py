from distutils.core import setup

setup(
    name='NlpToolkit-DataGenerator',
    version='1.0.3',
    packages=['DataGenerator', 'DataGenerator.Attribute', 'DataGenerator.CorpusGenerator',
              'DataGenerator.DatasetGenerator', 'DataGenerator.InstanceGenerator'],
    url='https://github.com/StarlangSoftware/DataGenerator-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Classification dataset generator library for high level Nlp tasks',
    install_requires=['NlpToolkit-AnnotatedSentence', 'NlpToolkit-AnnotatedTree', 'NlpToolkit-Classification',
                      'NlpToolkit-MorphologicalDisambiguation']
)
