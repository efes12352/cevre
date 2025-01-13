import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command("ekosistem")
async def ekosistem(ctx): 
    await ctx.send("Ekosistem, canlılar (biyotik) ve cansız (abiyotik) çevre arasında etkileşimlerin gerçekleştiği bir birimdir. Bir ekosistem, belirli bir alan içindeki bitkiler, hayvanlar, mikroorganizmalar ve çevresel unsurların birbirleriyle ve çevreleriyle olan ilişkilerini içerir. Ekosistemler, enerji akışı ve madde döngüsü gibi süreçlerle birbirine bağlıdır.")


@bot.command()
async def zarar(ctx): 
    await ctx.send("Zarar, çevresel ve biyotik bir etkiye sebep olan bir şeydir. Zararlar, çevresel hastalıklar, hırsızlıklar, ve kötüye yol açan maddeler gibi etkileri gösterir. Örnekler: kötüye yol açan maddeler, asitler, klorürler, klorofil, tuz, ve yağ gibi maddeler; çevresel hastalıklar, yıllık yakalanma sayısını ve yıllık ölümleri artıran hastalıklar; hırsızlıklar, yıllık ülkedeki hastalık sayısını ve yıllık ölümleri artıran hastalıklar.")

@bot.command()
async def cevre(ctx):
    await ctx.send("Çevre, çevresel ve biyotik bir etkiye sebep olan bir alan, alanın dışarısına ve dışarıya çıkan maddelerle olan ilişkilerini içerir. Örnekler: ��evredeki maddeler, asitler, klorürler, klorofil, tuz, ve yağ gibi maddeler; çevredeki etkiler, yıllık yakalanma sayısını ve yıllık ölümleri artıran hastalıklar; hırsızlıklar, yıllık ülkedeki hastalık sayısını ve yıllık ölümleri artıran hastalıklar.")





bot.run("token burda,Kamu spotu:Kimseyle paylaşmayın")
