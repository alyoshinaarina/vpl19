# KEYWORDER TELEGRAM BOT (t.me/Key_words_bot)

## Welcome to Keyworder Telegram bot. It provides a list of keywords for a document sent. 

### HOW DO I USE IT? 
In order to use our bot you have to dowload the following files:
- frequency.json 
- keyworder.py
- setup.py

Make sure they are in the same repository and run keyworder.py. As long as the code is in execution, you can chat with Keyworder bot (@Key_words_bot). Follow instructions it sends you (\help)

In order to make process more comportable, console logging is enabled.

### HOW DOES IT WORK? 
Keyworder compares a file you send it and National Russial Language Corpora in terms word frequency. It is estimated that those words which possess chi-squared value less than 0.003932 appear to be significant in determining the category of the text given. However, only top of the list Keyworder provides is likely to be considered actual keywords. For more detailes access google.com.

**NB: for some computers it is not enough to use built-in proxy to process a file. In this case, use your VPN.**

*Sometimes built-in proxy gets overloaded and stops working. If that occurs, contact Marina Kazyulina or use **kw detection.py***

### HOW DO I USE IT WITHOUT ALL THAT TELEGRAM BOT THING?
If you did not happen to have your Telegram account or dislike the idea of chatting with bot for some reason, there is still a way for you to automatically detect key words in your text. For this purpose dowload the following:
+ 'kw_detection.py" 
+ "frequencies.json"

Make sure they share the same folder. Add the file you want to know key words of, **replace "file.txt"** in the code (follow comments in code) and voila, your keywords are ready to be discovered. 


#### AND WHAT ARE ALL OF THOSE FILES FOR? 
+ **README.md** is for everyone to get the idea of what is going on in this repository. 
+ **ugrams from ruscorpora.txt** is a list of unigrams and the number of their entrances provided by ruscorpora.ru. 
+ **frequencies.py** is a python file which describes the process of creating **frequencies.json**.
+ **frequencies.json** is a json file containing information of all the lemmas and the number of their entrances in ruscorpora.
+ **kw detection.py** is a python file that containes code for detecting all of the significant words in the **file.txt** and outputs it on console. 
+ **file.txt** is an example of the file that **kw detection.py** processes. 
+ **setup.py** containes token and proxy for @Key_words_bot to work.
+ **keyworder.py** is a script which allows @Key_words_bot to work and loggs every action on console. 

##### Special thanks to Arina!!!
We would like to say thank you for such an interesting task, it was a pleasure to do it! 
While planning and trying to realize all of our aspirations, we learned:
+ how to work with Jupiter Notebook
+ how to work with Kaggle
+ what is GPU and why it didn't appear helpful
+ that servers may be stubborn and all the tfidf dreams are to crush against 429
+ how to use chi-squared and why
+ how to make Telegram bot accept files

and so on!

So... if you liked our project, please, let us know! We've been working so hard and we'd like to be aware whether it turned out to be good. 

