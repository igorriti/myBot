# My bot 

This is a chatbot made with RASA as a special practical work for the Exploratory Programming subject at the university.

The goal of it was to replicate myself (sort of like Gilfoyle does in Silicon Valley) and be able to answer things about myself, the university and more using not only rasa and its custom actions but also PROLOG.

## Features

General list of things the bot does:
- Answer typical questions and in some cases why
- Have a contact book (Currently I only save the name but a lot of things could be saved)
- Send audio via Telegram as a voice message
- Send stickers via Telegram
- Query PROLOG through Python
- Generate random videos from a YT channel to recommend it to you (I tried to make you a summary of it with GPT-3 but it didn't work out)
## Deployment

As you read, the bot is made to be deployed on Telegram. Here the [RASA documentation](https://rasa.com/docs/rasa/connectors/telegram/) in which it explains well the steps to follow
## To keep in mind

For the chatbot to work, you have to modify the RASA library, specifically in the path yourenv\RASA\Lib\site-packages\rasa\core\channels the channel.py file.

You have to modify the get_metadata function so that it looks like this:
 ```bash
     def get_metadata(self, request: Request) -> Optional[Dict[Text, Any]]:
        metadata = request.json
        return metadata
```

Also, you have to generate a Youtube api key with Google Cloud
## Lessons Learned

In the process of programming this chatbot, I learned better how they work and how they are composed. I was also able to reinforce my knowledge of Python and learn a bit of PROLOG.

I was amazed at the potential that RASA has and the wide range of things that can be done. Maybe I would have liked the documentation page to be better because for some things I had to search and investigate A LOT
