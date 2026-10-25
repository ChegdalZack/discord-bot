import discord
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Retrieve token and log channel ID from environment variables
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")

if not TOKEN:
    raise ValueError("No DISCORD_BOT_TOKEN found in environment variables.")
if not LOG_CHANNEL_ID:
    raise ValueError("No LOG_CHANNEL_ID found in environment variables.")

LOG_CHANNEL_ID = int(LOG_CHANNEL_ID)

# Set up intents
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("Bot is ready and listening for voice channel activity...")

@client.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    # Ignore bots if desired (optional, currently logs everyone)
    if member.bot:
        return

    log_channel = client.get_channel(LOG_CHANNEL_ID)
    if not log_channel:
        print(f"Error: Log channel with ID {LOG_CHANNEL_ID} not found.")
        return

    now = datetime.now()
    timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
    # Discord relative/absolute timestamp markdown tag
    discord_ts = int(now.timestamp())

    # 1. Joined a voice channel
    if before.channel is None and after.channel is not None:
        embed = discord.Embed(
            title="🎤 Voice Channel Joined",
            description=f"**{member}** joined **{after.channel.name}**",
            color=discord.Color.green()
        )
        embed.add_field(name="User", value=f"{member.mention} (`{member.id}`)", inline=True)
        embed.add_field(name="Channel", value=after.channel.name, inline=True)
        embed.add_field(name="Time", value=f"<t:{discord_ts}:F> (<t:{discord_ts}:R>)", inline=False)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Timestamp: {timestamp_str}")
        await log_channel.send(embed=embed)

    # 2. Left a voice channel
    elif before.channel is not None and after.channel is None:
        embed = discord.Embed(
            title="🚪 Voice Channel Left",
            description=f"**{member}** left **{before.channel.name}**",
            color=discord.Color.red()
        )
        embed.add_field(name="User", value=f"{member.mention} (`{member.id}`)", inline=True)
        embed.add_field(name="Channel", value=before.channel.name, inline=True)
        embed.add_field(name="Time", value=f"<t:{discord_ts}:F> (<t:{discord_ts}:R>)", inline=False)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Timestamp: {timestamp_str}")
        await log_channel.send(embed=embed)

    # 3. Switched voice channels
    elif before.channel is not None and after.channel is not None and before.channel != after.channel:
        embed = discord.Embed(
            title="🔄 Voice Channel Switched",
            description=f"**{member}** switched from **{before.channel.name}** to **{after.channel.name}**",
            color=discord.Color.orange()
        )
        embed.add_field(name="User", value=f"{member.mention} (`{member.id}`)", inline=True)
        embed.add_field(name="From", value=before.channel.name, inline=True)
        embed.add_field(name="To", value=after.channel.name, inline=True)
        embed.add_field(name="Time", value=f"<t:{discord_ts}:F> (<t:{discord_ts}:R>)", inline=False)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Timestamp: {timestamp_str}")
        await log_channel.send(embed=embed)

if __name__ == "__main__":
    client.run(TOKEN)
