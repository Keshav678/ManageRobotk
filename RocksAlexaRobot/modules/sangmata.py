# Added By Asad Ali

from telethon.errors.rpcerrorlist import YouBlockedUserError
from RocksAlexaRobot import telethn as tbot
from RocksAlexaRobot.events import register
from RocksAlexaRobot import ubot2 as ubot
from asyncio.exceptions import TimeoutError


@register(pattern="^/sg ?(.*)")
@register(pattern="^/check_name ?(.*)")
async def lastname(steal):
    steal.pattern_match.group(1)
    puki = await steal.reply("```Retrieving Such User Information..```")
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await puki.edit("```Please Reply To User Message.```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await puki.edit("```Reply To Real User's Message.```")
        return
    await puki.edit("```Please wait...```")
    try:
        async with ubot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "```Error, report to @WorldChattingFriendsWCF```"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await puki.edit(f"`{r.message}`")
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                ) 
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await puki.edit("```I Can't Find This User's Information, This User Has Never Changed His Name Before.```")
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await puki.edit(f"```{response.message}```")
            await ubot.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await puki.edit("`I'm Sick Sorry...`")

__help__ = """
 *Sangmata Module...*
 - `/sg` check previous detail of user.
"""

__mod_name__ = "💳 sᴀɴɢᴍᴀᴛᴀ"
