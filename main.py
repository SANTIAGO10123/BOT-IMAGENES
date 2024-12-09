import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await ctx.send("Archivo guardado...")
            await attachment.save(f"./{file_name}")
            try:
                clase = get_class("keras_model.h5", "labels.txt", file_name)
                if clase[0] == "CARRO NORMAL":
                    await ctx.send("Un carro normal en Colombia es un vehículo de transporte terrestre que generalmente tiene cuatro ruedas y es utilizado para el desplazamiento de personas y mercancías. Estos vehículos son comunes en las ciudades y en las zonas rurales, y pueden ser de diferentes tipos, como sedanes, SUV o camionetas. Los carros en Colombia suelen ser de marcas reconocidas como Chevrolet, Renault y Mazda, y son esenciales para la movilidad diaria de los colombianos.")
                
                elif clase[0] == "TAXI":
                    await ctx.send("Un TAXI es un medio de transporte público que se caracteriza por tener tarifas reguladas y ofrecer servicios de transporte de pasajeros en vehículos con conductor. Aquí te dejo algunos aspectos clave sobre los taxis en Colombia: 1. **Características del vehículo**: - Generalmente, los taxis son vehículos compactos y de colores distintivos, como el amarillo en muchas ciudades, lo que los hace fácilmente identificables. - Los modelos más comunes incluyen marcas como **Chevrolet**, **Renault** y **Citroën**. 2. **Funcionamiento**: - Los taxis operan con un **taxímetro**, que mide la distancia recorrida y calcula la tarifa correspondiente. - En algunas ciudades, también se pueden solicitar taxis a través de aplicaciones móviles, lo que facilita el proceso de llamada y pago. 3. **Disponibilidad**: - En ciudades como **Bogotá**, los taxis están disponibles las **24 horas del día**, y los usuarios pueden fijar su propio destino sin restricciones de rutas. 4. **Seguridad**: - Es recomendable tomar precauciones al usar taxis, como verificar que el vehículo tenga el **logotipo oficial** y que el taxímetro esté en funcionamiento. - También se aconseja no aceptar ayuda de extraños al abordar un taxi. 5. **Costo**: - Las tarifas son reguladas por las autoridades locales, y el costo puede variar según la ciudad y el tiempo del día. En resumen, los taxis en Colombia son una opción conveniente y accesible para el transporte urbano, con un sistema de tarifas reguladas y una amplia disponibilidad.")
            
            except:
                await ctx.send("Ha ocurrido un error, seguro que usaste una imagen???...")
    else:
        await ctx.send("Olvidaste subur una imagen...")

bot.run("")
