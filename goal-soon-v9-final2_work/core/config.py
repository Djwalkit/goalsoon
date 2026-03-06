import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_FOOTBALL_KEY","")
BASE_URL = "https://v3.football.api-sports.io"

SCORE_MODE = os.getenv("SCORE_MODE","DRAW")
MAX_DRAW_TOTAL_GOALS = int(os.getenv("MAX_DRAW_TOTAL_GOALS","6"))