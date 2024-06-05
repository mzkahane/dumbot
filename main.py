import discord
from discord.ext import commands
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel


def setup():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Running on", device)

    model = GPT2LMHeadModel.from_pretrained("gpt2").to(device)

    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    model.generation_config.pad_token_id = tokenizer.eos_token_id

    return device, model, tokenizer

def generate(device, model, tokenizer, prompt):
    input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)

    output = model.generate(
        input_ids, 
        max_length=100, 
        num_return_sequences=1, 
        no_repeat_ngram_size=2, 
        early_stopping=True,
        num_beams=10
    )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text
    
def main():
    device, model, tokenizer = setup()
   
    intents = discord.Intents().all()

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')

    @bot.command()
    async def dumb(ctx, *, prompt: str):
        response = generate(device, model, tokenizer, prompt)
        await ctx.send(response)

    @bot.command()
    @commands.is_owner()
    async def shutdown(ctx):
        await ctx.send("Shutting down...")
        exit()

    bot.run("MTI0Nzk3NzkyNzUyMjUyMTIxMQ.G0iN_e.Ekp2i0jnx-3Ny5EBpTdytmzlPPSL-rowgBjQkI")

main()