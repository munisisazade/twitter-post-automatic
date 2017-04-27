# README #

# Twitter Post Bot #
### --- How to install and use it ###
First you need to install python3 and after install django you can run the project following bellow steps 
```
#!

$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev
```

### --- Basic usage ###
You need to install Twython module for python or python3 use easy_install or pip 
```
#!
$ sudo pip3 install twython && sudo pip install twython
$ git clone https://github.com/munisisazade/twitter-post-automatic.git
$ cd twitter-post-automatic
$ python twitter_bot.py
```

### --- Advance usage  ###
If you want to Run this scripts forever use nodejs npm forever module 
```
#!
$ npm install forever -g
$ sudo ln -s /usr/bin/nodejs /usr/bin/node
$ git clone https://github.com/munisisazade/twitter-post-automatic.git
$ cd twitter-post-automatic
$ forever start -c python twitter_bot.py
$ # if you want to stop background prosess just type this
$ forever stopall
```
### --- Credits & Helpers ###

1. Use that script with forever - http://stackoverflow.com/a/18335151/968751
2. Twython module - https://twython.readthedocs.io/en/latest/


