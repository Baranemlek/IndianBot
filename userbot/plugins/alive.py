"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

name = str(ALIVE_NAME)
INDIANBOT_IS_ALIVE = ("**Apun Zinda He Sarr ^.^** \n`🇮🇳BOT Status : ` **☣Hot**\n\n"
                     f"`My peru owner`: {name}\n\n"
                     "`Indian Bot Version:` **3.8.7**\n`Python:` **3.8.5**\n"
                     "`Database Status:` **😀ALL OK**\n\n`Always with you, my master!\n`"
                     "**Bot Creator:** [🇮🇳INDIAN BHAI](t.me/pureindialover)\n"
                     "**Co-Owner:** [🇮🇳AKASH](t.me/AKASH_AM1)\n\n"
                     "     [🇮🇳Deploy This IndianBot🇮🇳](https://github.com/indianbhaiya/IndianBot)") 

@borg.on(admin_cmd(pattern="alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.forward_messages(alive.chat_id, 177, -1001473872047)
    await borg.send_message(chat, INDIANBOT_IS_ALIVE) 

