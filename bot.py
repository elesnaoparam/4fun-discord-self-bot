import asyncio
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'Fez login como {client.user}')
    channel = client.get_channel(id do chat)
    if channel:
        await simulate_typing(channel)
    else:
        print("Canal não encontrado.")

async def simulate_typing(channel):
    while True:
        try:
            async with channel.typing():
                await asyncio.sleep(2)

        except Exception as e:
            print(f"Ocorreu um erro durante a simulação de digitação: {e}")
@client.event
async def on_disconnect():
    print('Desconectado do Discord, tentando reconectar...')
    while not client.is_closed():
        try:
            await client.login('token da conta', bot=True)
            print('Reconectado com sucesso!')
            break
        except Exception as e:
            print(f'Falha ao reconectar: {e}')
            await asyncio.sleep(5)

client.run('token da conta')