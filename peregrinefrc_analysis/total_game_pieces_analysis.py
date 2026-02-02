from os import getenv
import pandas
from peregrine_client import PeregrineClient
from analysis import make_team_dataframe
from analysis_2023 import COUNT_FUNCTIONS, COUNT_NAMES

EVENT_ID = "2025wass"


client = PeregrineClient()
client.authenticate(
    username = "Alava", password = "heyisaac"
)
df = make_team_dataframe(
    client, EVENT_ID, COUNT_NAMES, COUNT_FUNCTIONS
)
print(df)
