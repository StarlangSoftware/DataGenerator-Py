Data Generator
============

Video Lectures
============

[<img src=https://github.com/StarlangSoftware/DataGenerator/blob/master/video1.jpg width="50%">](https://youtu.be/E9rE_eCffPE)[<img src=https://github.com/StarlangSoftware/DataGenerator/blob/master/video2.jpg width="50%">](https://youtu.be/ISHmGWvHL7k)

For Developers
============

You can also see [Cython](https://github.com/starlangsoftware/DataGenerator-Cy), [Java](https://github.com/starlangsoftware/DataGenerator), [Swift](https://github.com/starlangsoftware/DataGenerator-Swift), [Js](https://github.com/starlangsoftware/DataGenerator-Js), [C++](https://github.com/starlangsoftware/DataGenerator-CPP),  or [C#](https://github.com/starlangsoftware/DataGenerator-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Pip Install

	pip3 install NlpToolkit-DataGenerator

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called DataGenerator will be created. Or you can use below link for exploring the code:

	git clone https://github.com/starlangsoftware/DataGenerator-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `DataGenerator-PY` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============

+ [AnnotatedDataSetGenerator](#annotateddatasetgenerator)
+ [InstanceGenerator](#instancegenerator)

## AnnotatedDataSetGenerator

DataSet yaratmak için AnnotatedDataSetGenerator sınıfı önce üretilir.

	AnnotatedDataSetGenerator(self, folder: str, pattern: str, instanceGenerator: InstanceGenerator)

Ardından generate metodu ile DataSet yaratılır.

	generate(self) -> DataSet

## InstanceGenerator

DataGeneratorlerin InstanceGeneratorlere ihtiyacı vardır. Bunlar bir tek kelimeden bir 
Instance yaratan sınıflardır.

	generateInstanceFromSentence(self, sentence: Sentence, wordIndex: int) -> Instance

NER problemi için NerInstanceGenerator, FeaturedNerInstanceGenerator ve 
VectorizedNerInstanceGeneratorsınıfı

ShallowParse problemi için ShallowParseInstanceGenerator, 
FeaturedShallowParseInstanceGenerator ve VectorizedShallowParseInstanceGenerator sınıfı

WSD problemi için SemanticInstanceGenerator, FeaturedSemanticInstanceGenerator ve
VectorizedSemanticInstanceGenerator sınıfı

Morphological Disambiguation problemi için FeaturedDisambiguationInstanceGenerator sınıfı

## Example Generated DataSet

### Word Sense Disambiguation Task

The following Table shows the sample text represented with sense labels and three possible features, namely the root form of the word, the part of speech (POS) tag of the word, and a boolean feature for checking the capital case.

|Word|Root|Pos|Capital|...|Tag|
|---|---|---|---|---|---|
|Yüzündeki|yüz|Noun|True|...|yüz<sup>3</sup>|
|ketçap|ketçap|Noun|False|...|ketçap<sup>1</sup>|
|lekesi|leke|Noun|False|...|leke<sup>2</sup>|
|yüzdükten|yüz|Verb|False|...|yüz<sup>2</sup>| 
|sonra|sonra|PCAbl|False|...|sonra<sup>1</sup>| 
|çıkmış|çık|Verb|False|...|çık<sup>10</sup>|
|.|.|Punctuation|False|...|.<sup>1</sup>|

### Named Entity Recognition Task

The following Table shows the sample text represented with tag labels and three possible features, namely the root form of the word, the part of speech (POS) tag of the word, and a boolean feature for checking the capital case.

|Word|Root|Pos|Capital|...|Tag|
|---|---|---|---|---|---|
|Türk|Türk|Noun|True|...|ORGANIZATION|
|Hava|Hava|Noun|True|...|ORGANIZATION|
|Yolları|Yol|Noun|True|...|ORGANIZATION|
|bu|bu|Pronoun|False|...|NONE|
|Pazartesi'den|Pazartesi|Noun|True|...|TIME|
|itibaren|itibaren|Adverb|False|...|NONE|
|İstanbul|İstanbul|Noun|True|...|LOCATION|
|Ankara|Ankara|Noun|True|...|LOCATION|
|güzergahı|güzergah|Noun|False|...|NONE|
|için|için|Adverb|False|...|NONE|
|indirimli|indirimli|Adjective|False|...|NONE|
|satışlarını|sat|Noun|False|...|NONE|
|90|90|Number|False|...|MONEY|
|TL'den|TL|Noun|True|...|MONEY|
|başlatacağını|başlat|Noun|False|...|NONE|
|açıkladı|açıkla|Verb|False|...|NONE|
|.|.|Punctuation|False|...|NONE|

### Shallow Parse Task

The following Table shows the sample text represented with chunk labels and three possible features, namely the root form of the word, the part of speech (POS) tag of the word, and a boolean feature for checking the capital case.

|Word|Root|Pos|Capital|...|Tag|
|---|---|---|---|---|---|
|Türk|Türk|Noun|True|...|ÖZNE|
|Hava|Hava|Noun|True|...|ÖZNE|
|Yolları|yol|Noun|True|...|ÖZNE|
|Salı|Salı|Noun|True|...|ZARF TÜMLECİ|
|günü|gün|Noun|False|...|ZARF TÜMLECİ|
|yeni|yeni|Adjective|False|...|NESNE|
|indirimli|indirimli|Adjective|False|...|NESNE|
|fiyatlarını|fiyat|Noun|False|...|NESNE|
|açıkladı|açıkla|Verb|False|...|YÜKLEM|
|.|.|Punctuation|False|...|HİÇBİRİ|

## Cite
If you use this resource on your research, please cite the following paper: 

```
@article{acikgoz,
  title={All-words word sense disambiguation for {T}urkish},
  author={O. Açıkg{\"o}z and A. T. G{\"u}rkan and B. Ertopçu and O. Topsakal and B. {\"O}zenç and A. B. Kanburoğlu and {\.{I}}. Çam and B. Avar and G. Ercan and O. T. Y{\i}ld{\i}z},
  journal={2017 International Conference on Computer Science and Engineering (UBMK)},
  year={2017},
  pages={490-495}
}
@inproceedings{ertopcu17,  
	author={B. {Ertopçu} and A. B. {Kanburoğlu} and O. {Topsakal} and O. {Açıkgöz} and A. T. {Gürkan} and B. {Özenç} and İ. {Çam} and B. {Avar} and G. {Ercan} and O. T. {Yıldız}},  
	booktitle={2017 International Conference on Computer Science and Engineering (UBMK)},  title={A new approach for named entity recognition},   
	year={2017},  
	pages={474-479}
}
