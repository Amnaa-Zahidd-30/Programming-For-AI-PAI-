import requests
import json
try:
    with open("API.txt", "r") as file:
        apiurl=file.read().strip()
    response=requests.get(apiurl)
    if response.status_code!= 200:
        print("HTTP Error:",response.status_code)
        print("Response text:",response.text)
    else:
        data= response.json()
        print("\nAPI Summary")
        for key,value in data.items():
            if key!="data" and key!= "apikey":
                print(key,":",value)
        if data.get("status")=="success" and "data" in data and data["data"]:
            print("\nLive Matches")
            for match in data["data"]:
                print("Match Name:",match.get("name"))
                print("Status:",match.get("status"))
                print("Venue:",match.get("venue"))
                print("Date:",match.get("date"))

                if "score" in match and match["score"]:
                    for inning in match["score"]:
                        print("Inning:",inning.get("inning"))
                        print("Runs:",inning.get("R"))
                        print("Wickets:",inning.get("W"))
                        print("Overs:",inning.get("O"))
        else:
            print("\nAPI reported failure.")
            print("Reason:",data.get("reason", "No reason provided."))
except requests.exceptions.RequestException as e:
    print("\nNetwork Error:Could not connect to the API.")
    print("Details:",e)
except Exception as e:
    print("\nAn unexpected error occurred:",e)
