import discord
from discord.ext import commands
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel


def setup():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Running on", device)

    model = GPT2LMHeadModel.from_pretrained("gpt2").to(device)

def generate(device, model, prompt):
    input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)

    output = model.generate(
        input_ids, 
        max_length=100, 
        num_return_sequences=1, 
        no_repeat_ngram_size=2, 
        early_stopping=True
    )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text
    
def main():
    # bot = commands.Bot(command_prefix='!')

    # @bot.event
    # async def on_ready():
    #     print(f'Logged in as {bot.user.name}')

    # @bot.command()
    # async def talk(ctx, *, prompt: str):
    #     response = generate(device, model, prompt)
    #     await ctx.send(response)
    setup()

    prompt = "to be or not to be"

    response = generate(device, model, prompt)
    print(response)

main()