# 250201092

import sys

outlook = sys.argv[1]
temperature = sys.argv[2]
humidity = sys.argv[3]
windy = sys.argv[4]
playable = "No"

if outlook == "sunny":
    if humidity == "normal":
        playable = "Yes"
elif outlook == "overcast":
    playable = "Yes"
elif outlook == "rain":
    if windy == "false":
        playable = "Yes"

print("Play:", playable)
