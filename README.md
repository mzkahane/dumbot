# dumbot
Discord bot using a poorly trained LLM to give nonsense responses. The bot is powered by a pretrained GPT2 model with no fine tuning.

Currently, it is really good at completing sentences, it is really bad at answering questions...
## Usage
Once running and connected, any user can type `!dumb` followed by the question/prompt to give to dumbot, and it will respond in a few seconds.

To stop the bot, only the owner (will change in the future) can type `!shutdown` to cleanly disconnect.
## Future work
My first major goal is to Fine tune the model using a portion of an otherwise very large dataset of conversations from several arbitrary discord servers.

My second goal is to clean up the discord user experience of the bot. This would include some decorations to the bot's profile, appearance, and messages. Since the dataset teaches dumbot to sometime refer to the users in the training dataset conversations, I would also like to think of a way to change those into users of the current server.

My third goal is to add more functionality to the bot beyond being a chatbot (dice rolls, ping, poke, help, etc.)

## Disclaimer
This is a project I have been working on in my free time, to sharpen my LLM and Python skills, and learn about Discord bots. I am sure there are better ways to do some things, but thats the fun of learning!
The bot is intended to be used among me and my friends. If you'd like to use it in your server, just ask! It is not perfect and probably never will be however... You've been warned!

## Dataset
discord-data

author:       Jess Fan

title:        Discord Dataset

contact:      jeefan@ucsc.edu, contact@j-fan.ml

year:         2021

howpublished: https://www.kaggle.com/jef1056/discord-data

note: V5

