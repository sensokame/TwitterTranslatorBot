# TwitterTranslatorBot
This is a twitter bot implementation in python that answers to tweets when mentioned and translates the tweet that the mention tweet replies to.

## How to use

- create a twitter developer account
- fill the access and consumer tokens of the app found at ``bot.py``
- deploy the bot to (either locally or to a python deployment server like heruko)
- install the requirements found in ``requirements.txt``
- have ``bot.py`` run

the bot will loop infinitly and every two seconds it will check for mentions since the last id it has responded to (stored in ``last_seen_id.txt`` file). when the bot is mentioned it will take the parent tweet, translate it and answer to the tweet.  
for now, for the bot to work effectively, you need to specify the target and source languages using their code  

list of supported languages https://developers.google.com/admin-sdk/directory/v1/languages

sample use @bot_user_name fr en
where fr is the target language and en is the tweet language.

## Known issue

this library uses the translate library https://github.com/terryyin/translate-python and a known issue with that library is that the autodetect is broken, so when the auto detect is fixed in that library, this library can be updated to only require the target language instead of both languages.

## Contributing and License

This is an MIT project, you can fork and change the code however you like.  
you can contribute back to this project in the form of pull requests and/or issues
