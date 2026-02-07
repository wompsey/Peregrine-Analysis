from os import getenv
import pandas as pd
from peregrine_client import PeregrineClient
from analysis import make_team_dataframe
from analysis_2023 import COUNT_FUNCTIONS, COUNT_NAMES, COUNT_STATES_FUNC, COUNT_STATES_NAMES, COUNT_AUTO, COUNT_AUTO_NAMES, COUNT_TELE, COUNT_TELE_NAMES
from analysis_of_STATES import make_team_dataframes
from analysis_auto import make_team_dataframess
from analysis_teleop import make_team_dataframesss
EVENT_ID = "2025wass"


client = PeregrineClient()
client.authenticate(
    username = "Alava", password = "heyisaac"
)
df = make_team_dataframe(
    client, EVENT_ID, COUNT_NAMES, COUNT_FUNCTIONS
)
df2 = make_team_dataframes(client, EVENT_ID, COUNT_STATES_NAMES, COUNT_STATES_FUNC
)
df3 = make_team_dataframess(client, EVENT_ID, COUNT_AUTO_NAMES, COUNT_AUTO)
df4 = make_team_dataframesss(client, EVENT_ID, COUNT_TELE_NAMES, COUNT_TELE)
#print(df)
#updated_data = pd.concat([df, df2])

#updated_data.to_excel("scoutlist.xlsx")
with pd.ExcelWriter("scoutlist.xlsx", engine="openpyxl") as writer:
    df4.to_excel(writer, sheet_name="Teleop List")
    df3.to_excel(writer, sheet_name="Auto List") 
    df2.to_excel(writer, sheet_name="States List")
    df.to_excel(writer, sheet_name="Score List")
    
    
