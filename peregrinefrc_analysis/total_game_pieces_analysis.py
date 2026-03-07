from os import getenv
import pandas as pd
from peregrine_client import PeregrineClient
from analyzeData import make_team_dataframe
from getPieceData import COUNT_FUNCTIONS, COUNT_NAMES

from constants import username, password, eventID
EVENT_ID = eventID


client = PeregrineClient()
client.authenticate(
    username = username, password = password
)
pieces = make_team_dataframe(
    client, EVENT_ID, COUNT_NAMES, COUNT_FUNCTIONS
)


pieces.to_excel("scoutlist.xlsx")
    
    
    
