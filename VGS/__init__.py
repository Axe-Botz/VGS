from pyrogram import Client
from datetime import datetime
import time

StartTime = time.time()
START_TIME = datetime.now()
SUDO_USER = 6834053539


print("[INFO]: BOOTING UP!!")
API_ID = 20112715
API_HASH = "fe56c4634729f7c557b3298f0bb0cf1e"
STRING = "BQEy5UsAR81tgVTFRwMRWNMFCIwrqXO_m7Qw-6PL5Pa5l59lVCsUtpg42zeZyW0ojJvMs0GMr8bSpP60P63icXpmPBUJMX2IvVNx1I2iaefplrYE-4rqI5cdv55iUl2S0487oAS4XfNcYrn3VAouH6FWNCgn9S1tsHfmXLOC1dpGFj9dMyIxjvOsLTgT8tUTj_U313Dqk_oqbBwEQKSH2ePSiLSCvUW4boRN8SXPsT9uYK8B74wDymYjqe67kaUWJi9Dmdkub4YATx8XKLKexNxgpaecZlMAR1c4TaQcZBIpd_KlGDRiEBkqTa7fSxsa938LtYk_ASJD1zyhRhjJTJ5MVw3m3wAAAAGK8_CeAA"

userbot = Client(
  ":USERBOT:",
  api_id=API_ID,
  api_hash=API_HASH,
  session_string=str(STRING),
  plugins=dict(root="VGS/modules")
)



