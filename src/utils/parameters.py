# Environment
import os
from enum import Enum

from .model_name import ChatModelName


class HumanMode(Enum):
    DISCORD = "discord"
    STDIN = "stdin"


TIME_SPEED_MULTIPLIER = 1000
# Memory
RECENCY_WEIGHT = 1
SIMILARITY_WEIGHT = 1
IMPORTANCE_WEIGHT = 1
REFLECTION_MEMORY_COUNT = 50
PLAN_LENGTH = "24 hours"
DEFAULT_LOCATION_ID = os.getenv("DEFAULT_LOCATION_ID")
DEFAULT_WORLD_ID = os.getenv("DEFAULT_WORLD_ID")

DEFAULT_SMART_MODEL = (
    # ChatModelName.TURBO
    ChatModelName.GPT4
)
DEFAULT_FAST_MODEL = ChatModelName.TURBO
HUMAN_MODE = HumanMode.DISCORD


## DISCORD CHANNEL IDS
class DiscordChannelId(Enum):
    LOBBY = 1097591240733753365
    PARKING_LOT = 1097588240275484722
    PARK = 1097739840080056351
    WATER_COOLER = 1097587897252728935
    CONFERENCE_ROOM = 1097588427676979310
    COPY_ROOM = 1100222443320246465
    BREAK_ROOM = 1100222906857967696
    EXECUTIVE_SUITE = 1100223179366084628
    JANITORS_CLOSET = 1100223506597290094
    WORK_ZONE = 1100223988069838910
