import logging

from nextcord.ext.commands import Bot

from .user_activity import UserActivityTask


def start_all_loops(bot: Bot) -> None:
    UserActivityTask(bot).activity_voice_channels_check.start()
    logging.info('Tasks (loops) functions starting... OK')
