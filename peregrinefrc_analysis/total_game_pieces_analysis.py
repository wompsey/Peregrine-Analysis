from os import getenv
import pandas as pd
from peregrine_client import PeregrineClient
from analyzeData import make_team_dataframe
from getPieceData import COUNT_FUNCTIONS, COUNT_NAMES, rankNames
from rankTeams import make_team_dataframe as rankTeam_dataframe
from constants import username, password, eventID
EVENT_ID = eventID


client = PeregrineClient()
client.authenticate(
    username = username, password = password
)
pieces = make_team_dataframe(
    client, EVENT_ID, COUNT_NAMES, COUNT_FUNCTIONS
)
rankings = rankTeam_dataframe(
    client, EVENT_ID, rankNames, COUNT_FUNCTIONS
)
with pd.ExcelWriter("scoutlist.xlsx", engine="openpyxl") as writer:
    pieces.to_excel(writer, sheet_name="Scout List")
    rankings.to_excel(writer, sheet_name="Rankings")