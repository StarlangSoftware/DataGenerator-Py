from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='NlpToolkit-DataGenerator',
    version='1.0.5',
    packages=['DataGenerator', 'DataGenerator.Attribute', 'DataGenerator.CorpusGenerator',
              'DataGenerator.DatasetGenerator', 'DataGenerator.InstanceGenerator'],
    url='https://github.com/StarlangSoftware/DataGenerator-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Classification dataset generator library for high level Nlp tasks',
    install_requires=['NlpToolkit-AnnotatedSentence', 'NlpToolkit-AnnotatedTree', 'NlpToolkit-Classification',
                      'NlpToolkit-MorphologicalDisambiguation'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
