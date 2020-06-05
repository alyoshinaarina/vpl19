# KEYWORDER TELEGRAM BOT (t.me/Key_words_bot)

## Welcome to Keyworder Telegram bot. It provides a list of keywords for a document sent. 

### HOW DO I USE IT? 
In order to use our bot you have to dowload the following files:
- frequency.json 
- keyworder.py. 
- setup.py

Make sure they are in the same repository and run keyworder.py. As long as the code is in execution, you can chat with Keyworder bot (@Key_words_bot). Follow instructions it sends you (\help)

In order to make process more comportable, console logging is enabled.

### HOW DOES IT WORK? 
Keyworder compares a file you send it and National Russial Language Corpora in terms word frequency. It is estimated that those words which possess chi-squared value less than 0.003932 appear to be significant in determining the category of the text given. However, only top of the list Keyworder provides is likely to be considered actual keywords. For more detailes access google.com.

### HOW DO I USE IT WITHOUT ALL THAT TELEGRAM BOT THING?
If you did not happen to have your Telegram account or dislike the idea of chatting with bot for some reason, there is still a way for you to automatically detect key words in your text. For this purpose dowload the following:
+ 'kw_detection.py" 
+ "frequencies.json"

Make sure they share the same folder. Add the file you want to know key words of, **replace "file.txt"** in the code (follow comments in code) and voila, your keywords are ready to be discovered. 


#### AND WHAT ARE ALL OF THOSE FILES FOR? 
+ **README.md** is for everyone to get the idea of what is going on in this repository. 
+ **ugrams from ruscorpora.txt** are the list unigrams and the number of their entrances provided by ruscorpora.ru. 
+ **frequencies.py** is a python file which describes the process of creating **frequencies.json**.
+ **frequencies.json** is a json file containing information of all the lemmas and the number of their entrances in ruscorpora.
+ **kw detection.py** is a python file that containes code for detecting all of the dignificant words in the **file.txt** and outputs it on console. 
+ **setup.py** containes token and proxy for @Key_words_bot to work.
+ **keyworder.py** is a script which allows @Key_words_bot to work and loggs every action on console. 
