import os
from os import environ

# Your Auto Forward Channel ID's
FROM_CHANNELS = set(int(x)
                    for x in os.environ.get("FROM_CHANNELS", "").split())
TO_CHATS = set(int(x) for x in os.environ.get("TO_CHATS", "").split())

# required to Movies information
OMDB_KEY = environ.get("OMDB_KEY", "")

RE1TXT = os.environ.get("RE2TXT", "@Username"
RE2TXT = os.environ.get("RE2TXT", "@JESSEVERSE")
RE3TXT = os.environ.get("RE3TXT", "⚠️ Uploaded By @HQFilms4U")
RE4TXT = os.environ.get("RE4TXT", "@BollyWeBHolly")
RE5TXT = os.environ.get("RE5TXT", "@File_Movies_Uploaded")
RE6TXT = os.environ.get("RE6TXT", "@RunningMovies")

# text you want to replace with text above.
REPLACED = os.environ.get("REPLACED", "@Hollywood_0980")
