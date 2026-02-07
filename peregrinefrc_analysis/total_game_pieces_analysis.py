from os import getenv
import pandas as pd
from peregrine_client import PeregrineClient
from analyzePieces import make_team_dataframe
from getPieceData import COUNT_FUNCTIONS, COUNT_NAMES, COUNT_STATES_FUNC, COUNT_STATES_NAMES, COUNT_SCORE_NAMES
from analyzeRobotStates import make_team_dataframes
from analyzeScore import make_score_dataframe
from constants import username, password, eventID
EVENT_ID = eventID


client = PeregrineClient()
client.authenticate(
    username = username, password = password
)
pieces = make_team_dataframe(
    client, EVENT_ID, COUNT_NAMES, COUNT_FUNCTIONS
)
states = make_team_dataframes(client, EVENT_ID, COUNT_STATES_NAMES, COUNT_STATES_FUNC
)
score = make_score_dataframe(client, EVENT_ID, COUNT_SCORE_NAMES, COUNT_FUNCTIONS)

#print(df)
#updated_data = pd.concat([df, df2])

#updated_data.to_excel("scoutlist.xlsx")
with pd.ExcelWriter("scoutlist.xlsx", engine="openpyxl") as writer:

    score.to_excel(writer, sheet_name="Score List") 
    states.to_excel(writer, sheet_name="States List")
    pieces.to_excel(writer, sheet_name="Piece List")
    
    
