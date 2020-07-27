# Discord Bot
A discord bot using the Discord.py module by Rapptz, currently in development.

## Features:
* Censorship
* Message Counter
* Word Counter
* Random Website Generator

#### Currently in development:
* TTS narrator and Reddit API using PRAW

## Usage:
Replace token at the top of the file
```
TOKEN = "" # <--- insert token here
```
Run it, using python3 preferably, on any platform
```
python3 main.py
```

## Structure
The main file is universally adaptable to new cogs, which are features stored in the "cogs" folder. 

Cogs are structured as a specific Cog class using special decoraters, allowing for the bot to be adjustable to new commits.
