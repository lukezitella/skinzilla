import requests
import ctypes


# form of AK-47 | The Empress (Factory New)
hashes = [
    ("Skeleton Knife | Crimson Web", False),
    ("Butterfly Knife | Doppler", "Phase 2"),
    ("M4A1-S | Blue Phosphour", False),
    ("Talon Knife | Doppler", "Phase 2"),
    ("Flip Knife | Doppler", "Ruby"),
    ("Stiletto Knife | Doppler", "Sapphire"),
    ("Ursus Knife | Doppler", "Ruby"),
]
print("Past Examples:")
print(hashes)

hash = eval(input("enter (gun | skin,phase): "))
x = requests.get(
    "https://api.skinport.com/v1/sales/history",
).json()
names = []
i = 0

avg = 0
last = 0
for post in x:
    if post["market_hash_name"].find(hash[0]) != -1 and (
        hash[1] == False or post["version"] == hash[1]
    ):
        avg = post["last_90_days"]["avg"]
        last = post["last_24_hours"]["avg"]

        if last == None:
            last = post["last_7_days"]["avg"]

        if last != None:
            if last < 0.85 * avg:
                names.append(
                    post["market_hash_name"][post["market_hash_name"].find("(") :]
                )


if names == []:
    ctypes.windll.user32.MessageBoxW(
        0,
        "not below 85 percent of 90 RA or not sufficient volume in past 7 days to determine",
        "bruh moment",
        1,
    )
else:
    res = str(names) + ": 90 day avg: " + str(avg) + ", 24hr/7day avg: " + str(last)
    ctypes.windll.user32.MessageBoxW(
        0, res, "Last 24 hours below 85 percent of 90 day avg", 1
    )
