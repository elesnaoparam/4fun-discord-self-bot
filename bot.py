import asyncio
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'Fez login como {client.user}')
    channel = client.get_channel(ID DO CANAL)
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
        await asyncio.sleep(10)



@client.event
async def on_disconnect():
    print('Desconectado do Discord, tentando reconectar...')
    while not client.is_closed():
        try:
            await client.login('TOKEN DA CONTA', bot=True)
            print('Reconectado com sucesso!')
            break
        except Exception as e:
            print(f'Falha ao reconectar: {e}')
            await asyncio.sleep(5)

client.run('TOKEN DA CONTA')
