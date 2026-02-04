from os import getenv
import pandas as pd
from peregrine_client import PeregrineClient
from analysis import make_team_dataframe
from analysis_2023 import COUNT_FUNCTIONS, COUNT_NAMES
from analysis_2023 import COUNT_STATES_FUNC, COUNT_STATES_NAMES
from analysis_of_STATES import make_team_dataframes
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

#print(df)
#updated_data = pd.concat([df, df2])

#updated_data.to_excel("scoutlist.xlsx")
with pd.ExcelWriter("scoutlist.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Scout List")
    df2.to_excel(writer, sheet_name="States List")
