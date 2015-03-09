# UottawaOdesiUtils

Ceci est une librairie pour agir en tant que Helper pour travailler avec les Documentations xml d'Odesi. Le logiciel SPPS va abrégé toutes les phrases qui ont une taille plus grande que  251 caractères. Le but de cette libraire est de rendre plus facile de faire la traduction des `<labl>` et des balises `<qstnLit>` en créant un hash des valeurs des balises. Ensuite je pourrai savoir quel `<labl>` sera écourté en examinant la taille totale de caractères contenu dans cette balise et utilisé une application comme Flask/Django pour faire la traduction ou pour modifier la pharse écourtée par SPSS.

This is an utils library to work with DDI-xml. The purpose of this library is to ease the process of translating variable label in a document. This library will retrieve the `<labl>` and the `<qstnLit>` value of an IDD file and will also tell if the label.size is greater than 251 caracters, that will mean that it will be chopped in SPSS. So that it will be easy to create a json file, export it to a db for a Rails/Flask app. 

####Ruby
The ruby gem can be found [here](https://github.com/guinslym/uottawa_odesi_utils)

## Installation

	$ pip install pyodesiutils

Or install it yourself as:

    $ python setup.py

## Usage example

Dealing with one Documentation file
```python
>>> from pyodesiutils import retrieve_label_and_qstnlit
a = retrieve_label_and_qstnlit('esg-c-25.xml')
print(a[0])
>>>{'label_warning': False, 'variable_name': u'ABCDEF', 'qstnLit': u"Num\xe9ro d'identification de l'enregistrement.", 'label': u"Num\xe9ro d'identification de l'enregistrement."}
```

Comparing two files
```python
>>>from pyodesiutils import bilingual_files
	content = bilingual_files('esg-cycle-xx_fr.xml', 'gss-cycle-xx_en.xml')
	#french file must be first
	print(content[0])
	=> {
'label_warning_fr': False, 'variable_name': u'ABCDEF', 'qstnLit_fr': u"Num\xe9ro d'identification de l'enregistrement.", 'label_fr': u"Num\xe9ro d'identification de l'enregistrement.",
'label_warning_en': False, 'qstnLit_en': u"Record identification.", 'label_en': u"Record identification"	
}
```
Now it's easier to create a web app so that I can view the English and the French translation side-by-side and make corrections if the translation is not good enough or if the label size is greater than 251 character

##TODO
Flask app to put the json in a DB
Test file

## Contributing

1. Fork it ( https://github.com/guinslym/pyodesiutils/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
