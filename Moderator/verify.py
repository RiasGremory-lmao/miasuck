import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions
from discord.ext.commands import CheckFailure

checkrole = 948900826645155840
chung = 948785155558998056

class Verify(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Verify is working.')

    @commands.command()
    async def verify(self, ctx):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, id=checkrole)
        await ctx.author.add_roles(role)
        channel = self.client.get_channel(chung)
        await channel.send(
            f'''Chào mừng tên Lolicon {ctx.author.mention} đã đến với Vùng kín của chị Hằng. 
            Ở đây:
- Là nơi thân phận của bạn được định đoạt bằng cái mồm, và những kẻ level thấp hơn bạn thì không có quyền phản bác.

- Là sân chơi lành mạnh cho giới trẻ, có thể bẻ cong giới tính của bạn vào bất cứ lúc nào.

- Live show ca nhạc đặc sắc và bùng nổ vào những ngày lễ đặc biệt.

- Có cơ hội diện kiến và trò chuyện cùng những thành viên thuộc Hội Bảng Vàng Ranobe Việt Nam.

- Nơi những con nghiện và chẻ châu vi en thứ thiệt hội tụ.

- Đặc biệt hơn, nơi đây là đế đô của những tên cuồng loli, nơi mà nhạc Loli 24/7 lên ngôi và sở thích của bạn không bao giờ bị bash (ngoại trừ saki và koa chimbe).

  ''')
        await channel.send(file=discord.File('./file/intro.mov'))
        await channel.send(file=discord.File('./file/https://media2.giphy.com/media/hodAU4qrzFA80cbQWY/giphy.gif?cid=790b76119fb7d2a87e099a8cd9f99a2d3004f79b73fbb90c&rid=giphy.gif&ct=g'))

def setup(client):
    client.add_cog(Verify(client))
