from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("🍃️ 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 🍃️", data="help_back")
        ],
        [
        Button.url("⚡ 𝐂ʜᴀᴛ 𝐆ʀᴘ ⚡", "https://t.me/CODEX_KA_BAAP_4ST"),
        Button.url("🕸️ 𝐒ᴜᴘᴘᴏʀᴛ 🕸️", "https://t.me/I_M_FIGHTER")
        ],
        [
        Button.url("🍃🍷 𝖬𝖨𝖭𝖣~𝖦𝖠𝖬𝖦𝖤𝖱 🍷🍃", "https://t.me/ll4st_MIND_GAMERII")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**🕸️ ʜᴇʟʟᴏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n⌾ 𝗜 𝗔𝗠 [{BotName}](tg://user?id={BotId})​**\n╭───────────────────╮\n\n"
        TEXT += f"» **⚡ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ‣ [ᴛᴇᴀᴍ-4sᴛ](https://t.me/I_M_FIGHTER)**\n\n"
        TEXT += f"»️ **💦 𝗧𝗘𝝙𝗠 𝟰𝗦𝗧 || 𝗦𝗣𝝙𝗠​ ‣** `3.2`\n"
        TEXT += f"» ️**💦 𝗧𝗘𝝙𝗠 𝟰𝗦𝗧 || 𝗦𝗣𝝙𝗠​ ‣** `{telethon.__version__}`\n╰───────────────────╯"
        await event.client.send_file(
                event.chat_id,
                "https://telegra.ph/file/6268246c30fed8b0041e6.jpg",
                caption=TEXT, 
                buttons=PythonButton)
