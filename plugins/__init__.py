import os
from os import environ

# Your Auto Forward Channel ID's
FROM_CHANNELS = set(int(x)
                    for x in os.environ.get("FROM_CHANNELS", "").split())
TO_CHATS = set(int(x) for x in os.environ.get("TO_CHATS", "").split())

# required to Movies information
OMDB_KEY = environ.get("OMDB_KEY", "")

RE1TXT = os.environ.get("RE1TXT", "@Username1")
RE2TXT = os.environ.get("RE2TXT", "@Username1")
RE3TXT = os.environ.get("RE3TXT", "⚠️ Uploaded By @HQFilms4U")
RE4TXT = os.environ.get("RE4TXT", "@Username3")
RE5TXT = os.environ.get("RE5TXT", "@Username4")
RE6TXT = os.environ.get("RE6TXT", "@Username5")

# text you want to replace with text above.
REPLACED = os.environ.get("REPLACED", "@Hollywood_0980")

# MEDIA_FORWARD_ID = int(os.environ.get("MEDIA_FORWARD_ID"))
