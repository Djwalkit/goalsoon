from fastapi import FastAPI
from fastapi.responses import JSONResponse
from core.api_football import live_fixtures, fixture_stats
from core.model import pressure, probability

app = FastAPI()

def stat(block, team, name):
    try:
        arr = block[team]["statistics"]
        for s in arr:
            if s["type"] == name:
                v = s["value"]
                if v is None:
                    return 0
                if isinstance(v,str):
                    v = v.replace("%","").split("/")[0]
                return float(v)
    except:
        return 0
    return 0

@app.get("/api/ranked")
def ranked():
    items = []
    for f in live_fixtures():
        try:
            fixture = f["fixture"]
            minute = fixture["status"]["elapsed"] or 0
            teams = f["teams"]
            goals = f["goals"]
            if goals["home"] != goals["away"]:
                continue
            if goals["home"] + goals["away"] > 6:
                continue

            stats = fixture_stats(fixture["id"])
            if len(stats) < 2:
                continue

            sot = stat(stats,0,"Shots on Goal")+stat(stats,1,"Shots on Goal")
            shots = stat(stats,0,"Total Shots")+stat(stats,1,"Total Shots")
            corners = stat(stats,0,"Corner Kicks")+stat(stats,1,"Corner Kicks")
            dang = stat(stats,0,"Dangerous Attacks")+stat(stats,1,"Dangerous Attacks")
            xg = stat(stats,0,"Expected Goals")+stat(stats,1,"Expected Goals")

            p = pressure(sot,shots,corners,dang,xg)
            prob = probability(p, minute)

            items.append({
                "league": f["league"]["name"],
                "home": teams["home"]["name"],
                "away": teams["away"]["name"],
                "score": f"{goals['home']}-{goals['away']}",
                "minute": minute,
                "probability": prob
            })
        except:
            pass

    items.sort(key=lambda x: x["probability"], reverse=True)
    return JSONResponse(items)