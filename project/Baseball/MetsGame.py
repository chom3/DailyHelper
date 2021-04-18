import statsapi
from datetime import datetime, date, timezone, timedelta
import pytz

# Only care about the Mets

metsId = (statsapi.lookup_team("NYM"))[0]['id']

date_format = "%Y-%m-%dT%H:%M:%SZ" 
est_timezone = pytz.timezone('America/New_York')

def getStartTime(game_datetime):
    d = datetime.fromisoformat(game_datetime[:-1]).replace(tzinfo=pytz.utc) # we need to strip 'Z' before parsing
    return d.astimezone(est_timezone).strftime('%I:%M %p')

def getDailyMetsGameDetails():
    try:
        gameDetails = statsapi.schedule(date=None, start_date=datetime.today().strftime('%Y-%m-%d'), end_date=None, team=metsId, opponent="", sportId=1, game_id=None)[0]
    except IndexError as e:
        return "There's no Mets game today."

    metsAreHome = True if gameDetails['home_name'] == "New York Mets" else False

    opposingTeam = gameDetails['away_name'] if metsAreHome else gameDetails['home_name']
    # Get start time
    startTime = getStartTime(gameDetails['game_datetime'])

    # Mets starting pitcher
    metsStartingPitcher = gameDetails['home_probable_pitcher'] if (metsAreHome) else gameDetails['away_probable_pitcher']

    return f"\nStart time is {startTime}. The Mets are playing the {opposingTeam}. Today's pitcher is {metsStartingPitcher}."