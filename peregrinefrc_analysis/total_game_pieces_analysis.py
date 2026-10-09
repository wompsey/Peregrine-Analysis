from os import getenv
import pandas as pd
from peregrine_client import PeregrineClient
from analyzeData import make_team_dataframe
from getPieceData import COUNT_FUNCTIONS, COUNT_NAMES, rankNames
from rankTeams import make_team_dataframe as rankTeam_dataframe
from constants import username, password, eventID



client = PeregrineClient()
client.authenticate(
      username, password
)
pieces = make_team_dataframe(
    client, eventID, COUNT_NAMES, COUNT_FUNCTIONS
)
rankings = rankTeam_dataframe(
    client, eventID, rankNames, COUNT_FUNCTIONS
)
with pd.ExcelWriter("scoutlist.xlsx", engine="openpyxl") as writer:
    pieces.to_excel(writer, sheet_name="Scout List")
    rankings.to_excel(writer, sheet_name="Rankings")