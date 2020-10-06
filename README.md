# python-interactive-dictionary
This is an interactive dictionary, this gives the meaning of the word entered by the user, in case the word entered isn't correct or dosnt exist in the dictionary, it will prompt you with the closest word that exist.
## Instaling dependencies
```
import json
from difflib import get_close_matches
```
## key features of the programme
* written using basic knowledge of python
* extremely simple to interpret even for a beginner
* made use of a data.json file which contains the meanings of the words
* used get_close_matches from difflib to predict the closest word in case the one entered isnt present in the Json file
