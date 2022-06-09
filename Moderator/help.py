import discord
from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Help is working.')

    
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='HƯỚNG DẪN CỦA TEARMOON',
                              description='',
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name='moon:info <ping người khác nếu muốn>', value='Xem profile card', inline=False)
        embed.add_field(name='moom:setbg', value='Chỉnh bg cho profile card của mình', inline=False)
        embed.add_field(
            name='moon:mute <đối tượng> <thời gian> <lý do>',
            value='Nhốt ai đó vào tù (nếu không có thời gian sẽ là vĩnh viễn)',
            inline=False)
        embed.add_field(name='moon:unmute <đối tượng>',
                        value='Ân xá cho tù nhân',
                        inline=False)
        embed.add_field(name='moon:gamehelp', value='hướng dấn của game', inline=False)                
        embed.add_field(name='moon:musichelp', value='hướng dấn của nhạc', inline=False)      
        embed.add_field(name='moon:pinghelp', value='hướng dấn của ping và vanmau', inline=False)      
        await ctx.send(embed=embed)


    @commands.command()
    async def pinghelp(self, ctx):
        embed = discord.Embed(title='HƯỚNG DẪN CỦA TEARMOON',
                              description='',
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name='moon:ping', value='Gọi cho tôi', inline=False)
        embed.add_field(name='moon:listping', value='Danh sách các câu trả lời cá nhân của lênh ping', inline=False)
        embed.add_field(name='moon:addping <Câu trả lời>', value='Thêm câu trả lời cá nhân của lênh ping', inline=False)
        embed.add_field(name='moon:delping <số thứ tự>', value='Xóa câu trả lời cá nhân của lênh ping', inline=False)
        embed.add_field(
            name='moon:vanmau <đối tượng>',
            value=
            'Văn mẫu tất nhiên rồi!',
            inline=False)
        embed.add_field(name='moon:listvanmau', value='Danh sách văn mẫu', inline=False)
        embed.add_field(name='moon:addvanmau <văn mẫu>', value='Thêm văn mẫu', inline=False)
        embed.add_field(name='moon:delvanmau <số thứ tự>', value='Xóa văn mẫu', inline=False)
        

        await ctx.send(embed=embed)

    @commands.command()
    async def musichelp(self, ctx):
        embed = discord.Embed(title='HƯỚNG DẪN CỦA TEARMOON',
                              description='',
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name='moon:join', value='Mời bot vào voice', inline=False)
        embed.add_field(name='moon:play <tên bài hoặc link bài hát>', value='Bật nhac', inline=False)
        embed.add_field(name='moon:queue', value='Coi queue nhạc', inline=False)
        embed.add_field(name='moon:loop', value='Loop 1 bài nhạc', inline=False)
        embed.add_field(name='moon:queueloop', value='Loop queue', inline=False)
        embed.add_field(name='moon:remove <số thứ tự>', value='Xóa 1 bài nhạc trong queue', inline=False)
        embed.add_field(name='moon:skip', value='skip nhạc trong queue', inline=False)
        embed.add_field(name='moon:pause', value='Tạm dừng nhạc', inline=False)
        embed.add_field(name='moon:resume', value='Tiếp tục nhạc', inline=False)
        embed.add_field(name='moon:volume <số>', value='Chỉnh âm lượng', inline=False)
        
        await ctx.send(embed=embed)

    @commands.command()
    async def gamehelp(self, ctx):    
        embed = discord.Embed(title='HƯỚNG DẪN CỦA TEARMOON',
                              description='',
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name='moon:startYT', value='Coi Youtube cùng nhau qua discord?', inline=False)
        embed.add_field(name='moon:startPO', value='Poker cùng nhau qua discord?', inline=False)
        embed.add_field(name='moon:startCH', value='Cờ vua cùng nhau qua discord?', inline=False)
        embed.add_field(name='moon:startFI', value='Giả lập câu cá kiểu ngư dân Nha Trang cùng nhau qua discord?', inline=False)
        embed.add_field(name='moon:startAM', value='Among sú bản pha ke cùng nhau qua discord?', inline=False)
        embed.add_field(name='moon:startSC', value='Nối từ cực căng cùng nhau qua discord?', inline=False)
        
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Kick(client))