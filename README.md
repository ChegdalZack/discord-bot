<<<<<<< HEAD
# Discord Voice Logger Bot

A lightweight, robust Python bot built with `discord.py` that logs when server members join, leave, or switch voice channels, complete with exact timestamps and user avatars.

---

## Features

- **Voice Join Logging**: Records when a user enters a voice channel with timestamp and user mention.
- **Voice Leave Logging**: Records when a user leaves a voice channel.
- **Voice Switch Logging**: Records when a user moves from one voice channel to another.
- **Embed Support**: Clean, color-coded Discord embeds with thumbnails and relative timestamps (`<t:TIMESTAMP:R>`).

---

## Setup Instructions

### Step 1: Create a Discord Bot Application
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application** and give it a name (e.g., *VoiceLogger*).
3. Navigate to the **Bot** tab on the left sidebar:
   - Click **Reset Token** to generate your bot token. Copy and save this token securely.
   - Scroll down to **Privileged Gateway Intents** and enable:
     - **Server Members Intent** (`GUILD_MEMBERS`)
   - (Note: `GUILD_VOICE_STATES` is a standard intent and does not need to be toggled in the portal, but it is enabled automatically in the `bot.py` code).
4. Navigate to the **OAuth2 > URL Generator** tab:
   - Under **Scopes**, select `bot`.
   - Under **Bot Permissions**, select:
     - `View Channels`
     - `Send Messages`
     - `Embed Links`
   - Copy the generated URL at the bottom and open it in your browser to invite the bot to your Discord server.

### Step 2: Configure Environment Variables
Create a file named `.env` in the same folder as `bot.py` with the following contents:

```env
DISCORD_BOT_TOKEN=your_bot_token_here
LOG_CHANNEL_ID=your_text_channel_id_here
```

*Note:* To get your text channel ID in Discord, right-click your designated log channel and select **Copy Channel ID** (ensure Developer Mode is enabled in Discord settings under Advanced).

### Step 3: Install Dependencies
Open your terminal in the folder containing these files and run:

```bash
pip install -r requirements.txt --break-system-packages
```

### Step 4: Run the Bot
```bash
python bot.py
```
=======
# discord-bot
>>>>>>> 59bf691598be2a92c0b83c2c2a442257cbc426e7
