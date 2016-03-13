import requests
import json
import threading
from time import sleep


# Define Base URL
url = "http://A.B.C.D/jjcapi/api.php"


# Playfield Parameters
ground_list01 = ["f113"]
ground_list02 = ["f212","f213"]
ground_list03 = ["f311","f312","f313"]
ground_list04 = ["f410","f411","f412","f413"]
ground_list05 = ["f505","f506","f507","f508","f509","f510","f511","f512","f513","f514","f515","f516","f517"]
ground_list06 = ["f605","f606","f607","f608","f609","f610","f611","f612","f613","f614","f615","f616"]
ground_list07 = ["f705","f706","f707","f708","f709","f710","f711","f712","f713","f714","f715"]
ground_list08 = ["f805","f806","f807","f808","f809","f810","f811","f812","f813","f814"]
ground_list09 = ["f905","f906","f907","f908","f909","f910","f911","f912","f913"]
ground_list10 = ["f1004","f1005","f1006","f1007","f1008","f1009","f1010","f1011","f1012","f1013"]
ground_list11 = ["f1103","f1104","f1105","f1106","f1107","f1108","f1109","f1110","f1111","f1112","f1113"]
ground_list12 = ["f1202","f1203","f1204","f1205","f1206","f1207","f1208","f1209","f1210","f1211","f1212","f1213"]
ground_list13 = ["f1301","f1302","f1303","f1304","f1305","f1306","f1307","f1308","f1309","f1310","f1311","f1312","f1313"]
ground_list14 = ["f1405","f1406","f1407","f1408"]
ground_list15 = ["f1505","f1506","f1507"]
ground_list16 = ["f1605","f1606"]
ground_list17 = ["f1705"]
ground_list = ground_list01 + ground_list02 + ground_list03 + ground_list04 + ground_list05 + ground_list06 +ground_list07 + ground_list08 + ground_list09 + ground_list10 + ground_list11 + ground_list12 + ground_list13 + ground_list14 + ground_list15 + ground_list16 + ground_list17
ground = {}


# Startposition Parameters
startposition1 = ["f113","f212","f213","f311","f312","f313","f410","f411","f412","f413"]
startposition2 = ["f514","f515","f516","f517","f614","f615","f616","f714","f715","f814"]
startposition3 = ["f1013","f1112","f1113","f1211","f1212","f1213","f1310","f1311","f1312","f1313"]
startposition4 = ["f1405","f1406","f1407","f1408","f1505","f1506","f1507","f1605","f1606","f1705"]
startposition5 = ["f1004","f1103","f1104","f1202","f1203","f1204","f1301","f1302","f1303","f1304"]
startposition6 = ["f505","f506","f507","f508","f605","f606","f607","f705","f706","f805"]


# Create empty playground
def create_playground():
    for cnt_ground in ground_list:
        ground[cnt_ground] = 0


# Create start area 1
def create_startarea1(gameid):
    ball = 10
    groundstartposition = {}
    for cnt_startposition in startposition1:
        groundstartposition[cnt_startposition] = str(ball)
        ball += 1
    url_startarea = url + "/games/" + gameid
    response_startarea = requests.put(url_startarea,data=json.dumps(groundstartposition))


# Create start area 2
def create_startarea2(gameid):
    ball = 20
    groundstartposition = {}
    for cnt_startposition in startposition2:
        groundstartposition[cnt_startposition] = ball
        ball += 1
    url_startarea = url + "/games/" + gameid
    response_startarea = requests.put(url_startarea,data=json.dumps(groundstartposition))


# Create start area 3
def create_startarea3(gameid):
    ball = 30
    groundstartposition = {}
    for cnt_startposition in startposition3:
        groundstartposition[cnt_startposition] = ball
        ball += 1
    url_startarea = url + "/games/" + gameid
    response_startarea = requests.put(url_startarea,data=json.dumps(groundstartposition))


# Create start area 4
def create_startarea4(gameid):
    ball = 40
    groundstartposition = {}
    for cnt_startposition in startposition4:
        groundstartposition[cnt_startposition] = ball
        ball += 1
    url_startarea = url + "/games/" + gameid
    response_startarea = requests.put(url_startarea,data=json.dumps(groundstartposition))


# Create start area 5
def create_startarea5(gameid):
    ball = 50
    groundstartposition = {}
    for cnt_startposition in startposition5:
        groundstartposition[cnt_startposition] = ball
        ball += 1
    url_startarea = url + "/games/" + gameid
    response_startarea = requests.put(url_startarea,data=json.dumps(groundstartposition))


# Create start area 6
def create_startarea6(gameid):
    ball = 60
    groundstartposition = {}
    for cnt_startposition in startposition6:
        groundstartposition[cnt_startposition] = ball
        ball += 1
    url_startarea = url + "/games/" + gameid
    response_startarea = requests.put(url_startarea,data=json.dumps(groundstartposition))


# Allow the player to play and verify his move
def playercanplay(player,moveid,gameid):
    # Allow the player to play
    url_round_playercanplay = url + "/rounds/" + moveid
    payload_round_playercanplay = {player + "src":"1"}
    response_round_playercanplay = requests.put(url_round_playercanplay,data=json.dumps(payload_round_playercanplay))

    # Check if the player has moved
    while True:
        url_roundcheck = url + "/rounds?filter=id,eq," + moveid + "&transform=1"
        response_roundcheck = requests.get(url_roundcheck)
        response_roundcheck_json = response_roundcheck.json()

        # When the player has moved, verify the move
        if response_roundcheck_json["rounds"][0][player + "src"] != "1":
            failure = "no"
            success = "no"
            url_roundcheck2 = url + "/games?filter=id,eq," + gameid + "&transform=1"
            response_roundcheck2 = requests.get(url_roundcheck2)
            response_roundcheck2_json = response_roundcheck2.json()
            src_field = int(response_roundcheck_json["rounds"][0][player + "src"])
            dst_field = int(response_roundcheck_json["rounds"][0][player + "dst"])
            mid_field = int((src_field + dst_field)/2)

            # Check if source field exists
            if not "f" + str(src_field) in ground_list:
                #failure = "yes"
                return("notok")

            # Check if destination field exists
            elif not "f" + str(dst_field) in ground_list:
                return("notok")

            # Check if destination field is free
            elif response_roundcheck2_json["games"][0]["f" + str(dst_field)] != "0":
                return("notok")

            # Check if source field is not empty
            elif response_roundcheck2_json["games"][0]["f" + str(src_field)] == "0":
                return("notok")

            # Check if destination field is a neighbor
            elif dst_field == src_field+1 or dst_field == src_field-1 or dst_field == src_field+99 or dst_field == src_field-99 or dst_field == src_field+100 or dst_field == src_field-100:
                success = "yes"

            # Check if middle field is valid
            elif "f" + str(mid_field) in ground_list and response_roundcheck2_json["games"][0]["f" + str(mid_field)] != "0":
                dif_field = dst_field-src_field
                dif_field1 = dst_field-mid_field
                dif_field2 = mid_field-src_field

                if dif_field == 200 or dif_field == 400 or dif_field == 600 or dif_field == 800 or dif_field == 1000 or dif_field == 1200:
                    cnt_steps = dif_field1-100
                    while cnt_steps > 0:
                        if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+mid_field)] != "0":
                            failure = "yes"
                        cnt_steps-=100
                    cnt_steps = dif_field2-100
                    while cnt_steps > 0:
                        if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+src_field)] != "0":
                            failure = "yes"
                        cnt_steps-=100
                    success = "yes"

                elif dif_field == -200 or dif_field == -400 or dif_field == -600 or dif_field == -800 or dif_field == -1000 or dif_field == -1200:
                    cnt_steps = dif_field1+100
                    while cnt_steps < 0:
                        if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+mid_field)] != "0":
                            failure = "yes"
                        cnt_steps+=100
                    cnt_steps = dif_field2+100
                    while cnt_steps < 0:
                        if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+src_field)] != "0":
                            failure = "yes"
                        cnt_steps+=100
                    success = "yes"

                elif dif_field == 198 or dif_field == 396 or dif_field == 594 or dif_field == 792 or dif_field == 990 or dif_field == 1188:
                    cnt_steps = dif_field1-99
                    while cnt_steps > 0:
                        if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+mid_field)] != "0":
                            failure = "yes"
                        cnt_steps-=99
                    cnt_steps = dif_field2-99
                    while cnt_steps > 0:
                        if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+src_field)] != "0":
                            failure = "yes"
                        cnt_steps-=99
                    success = "yes"

                elif dif_field == -198 or dif_field == -396 or dif_field == -594 or dif_field == -792 or dif_field == -990 or dif_field == -1188:
                    cnt_steps = dif_field1+99
                    while cnt_steps < 0:
                        if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+mid_field)] != "0":
                            failure = "yes"
                        cnt_steps+=99
                    cnt_steps = dif_field2+99
                    while cnt_steps < 0:
                        if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+src_field)] != "0":
                            failure = "yes"
                        cnt_steps+=99
                    success = "yes"

                elif dif_field == 2 or dif_field == 4 or dif_field == 6 or dif_field == 8 or dif_field == 10 or dif_field == 12:
                    cnt_steps = dif_field1-1
                    while cnt_steps > 0:
                        if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+mid_field)] != "0":
                            failure = "yes"
                        cnt_steps-=1
                    cnt_steps = dif_field2-1
                    while cnt_steps > 0:
                        if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+src_field)] != "0":
                            failure = "yes"
                        cnt_steps-=1
                    success = "yes"

                elif dif_field == -2 or dif_field == -4 or dif_field == -6 or dif_field == -8 or dif_field == -10 or dif_field == -12:
                    cnt_steps = dif_field1+1
                    while cnt_steps < 0:
                        if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+mid_field)] != "0":
                            failure = "yes"
                        cnt_steps+=1
                    cnt_steps = dif_field2+1
                    while cnt_steps < 0:
                        if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+src_field)] != "0":
                            failure = "yes"
                        cnt_steps+=1
                    success = "yes"

            # If the step was successful, accept the move
            if success == "yes" and failure == "no":
                url_acceptmove = url + "/games/" + gameid
                payload_acceptmove = {"f" + str(src_field):"0", "f" + str(dst_field):response_roundcheck2_json["games"][0]["f" + str(src_field)]}
                response_acceptmove = requests.put(url_acceptmove,data=json.dumps(payload_acceptmove))
                return("ok")

            # If no valid path could be found, check for multiple jumps
            else:
                pathfeedback = verifypath(src_field,dst_field,response_roundcheck2_json,10)

                # If the path validation was successful, accept the move
                if pathfeedback == "ok":
                    url_acceptmove = url + "/games/" + gameid
                    payload_acceptmove = {"f" + str(src_field):"0", "f" + str(dst_field):response_roundcheck2_json["games"][0]["f" + str(src_field)]}
                    response_acceptmove = requests.put(url_acceptmove,data=json.dumps(payload_acceptmove))
                    return("ok")

                # If no valid path could be found, reject the move
                else:
                    return("notok")

        else:
            # Continue checking if a move have been made in one second
            sleep(1)
            continue


# Verify the path for multiple jumps
def verifypath(src_jmp_field,dst_field,response_roundcheck2_json,maxjumps):

    # Check all paths
    for cnt_verifypath in ground_list:
        dst_jmp_field = int(cnt_verifypath.strip("f"))
        mid_jmp_field = int((src_jmp_field + dst_jmp_field)/2)
        dif_jmp_field = dst_jmp_field-src_jmp_field
        dif_jmp_field1 = dst_jmp_field-mid_jmp_field
        dif_jmp_field2 = mid_jmp_field-src_jmp_field
        success = "no"
        failure = "no"

        # Check if destination field is free
        if response_roundcheck2_json["games"][0]["f" + str(dst_jmp_field)] != "0":
            failure = "yes"

        # Check if destination field is equal to the source field
        elif cnt_verifypath == "f" + str(src_jmp_field):
            failure = "yes"

        # Check if middle field is valid
        elif "f" + str(mid_jmp_field) in ground_list and response_roundcheck2_json["games"][0]["f" + str(mid_jmp_field)] != "0":

            if dif_jmp_field == 200 or dif_jmp_field == 400 or dif_jmp_field == 600 or dif_jmp_field == 800 or dif_jmp_field == 1000 or dif_jmp_field == 1200:
                cnt_steps = dif_jmp_field1-100
                while cnt_steps > 0:
                    if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+mid_jmp_field)] != "0":
                        failure = "yes"
                    cnt_steps-=100
                cnt_steps = dif_jmp_field2-100
                while cnt_steps > 0:
                    if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+src_jmp_field)] != "0":
                        failure = "yes"
                    cnt_steps-=100
                success = "yes"

            elif dif_jmp_field == -200 or dif_jmp_field == -400 or dif_jmp_field == -600 or dif_jmp_field == -800 or dif_jmp_field == -1000 or dif_jmp_field == -1200:
                cnt_steps = dif_jmp_field1+100
                while cnt_steps < 0:
                    if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+mid_jmp_field)] != "0":
                        failure = "yes"
                    cnt_steps+=100
                cnt_steps = dif_jmp_field2+100
                while cnt_steps < 0:
                    if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+src_jmp_field)] != "0":
                        failure = "yes"
                    cnt_steps+=100
                success = "yes"

            elif dif_jmp_field == 198 or dif_jmp_field == 396 or dif_jmp_field == 594 or dif_jmp_field == 792 or dif_jmp_field == 990 or dif_jmp_field == 1188:
                cnt_steps = dif_jmp_field1-99
                while cnt_steps > 0:
                    if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+mid_jmp_field)] != "0":
                        failure = "yes"
                    cnt_steps-=99
                cnt_steps = dif_jmp_field2-99
                while cnt_steps > 0:
                    if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+src_jmp_field)] != "0":
                        failure = "yes"
                    cnt_steps-=99
                success = "yes"

            elif dif_jmp_field == -198 or dif_jmp_field == -396 or dif_jmp_field == -594 or dif_jmp_field == -792 or dif_jmp_field == -990 or dif_jmp_field == -1188:
                cnt_steps = dif_jmp_field1+99
                while cnt_steps < 0:
                    if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+mid_jmp_field)] != "0":
                        failure = "yes"
                    cnt_steps+=99
                cnt_steps = dif_jmp_field2+99
                while cnt_steps < 0:
                    if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+src_jmp_field)] != "0":
                        failure = "yes"
                    cnt_steps+=99
                success = "yes"

            elif dif_jmp_field == 2 or dif_jmp_field == 4 or dif_jmp_field == 6 or dif_jmp_field == 8 or dif_jmp_field == 10 or dif_jmp_field == 12:
                cnt_steps = dif_jmp_field1-1
                while cnt_steps > 0:
                    if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+mid_jmp_field)] != "0":
                        failure = "yes"
                    cnt_steps-=1
                cnt_steps = dif_jmp_field2-1
                while cnt_steps > 0:
                    if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+src_jmp_field)] != "0":
                        failure = "yes"
                    cnt_steps-=1
                success = "yes"

            elif dif_jmp_field == -2 or dif_jmp_field == -4 or dif_jmp_field == -6 or dif_jmp_field == -8 or dif_jmp_field == -10 or dif_jmp_field == -12:
                cnt_steps = dif_jmp_field1+100
                while cnt_steps < 0:
                    if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+mid_jmp_field)] != "0":
                        failure = "yes"
                    cnt_steps+=100
                cnt_steps = dif_jmp_field2+100
                while cnt_steps < 0:
                    if response_roundcheck2_json["games"][0]["f" + str(cnt_steps+src_jmp_field)] != "0":
                        failure = "yes"
                    cnt_steps+=100
                success = "yes"

        # Everything else is a failure ;)
        else:
            failure = "yes"

        # Check if we reached the destination
        if success == "yes" and failure == "no" and dst_jmp_field == dst_field:
            return("ok")

        # Check if we reached the maximum number of jumps
        elif success == "yes" and failure == "no" and maxjumps > 0:
            maxjumps -= 1
            pathfeedback = verifypath(dst_jmp_field,dst_field,response_roundcheck2_json,maxjumps)
            if pathfeedback == "ok":
                return("ok")


# Set game to started
def game2(players,gameid):
    url_gamestarted = url + "/games/" + gameid
    payload_gamestarted = {"started":"1","round":"0"}
    response_gamestarted = requests.put(url_gamestarted,data=json.dumps(payload_gamestarted))
    url_round = url + "/rounds"

    # 2 players
    if players == "2":
        round = 1
        while True:

            # Start a new round
            payload_round = {"gameid":gameid,"round":str(round)}
            response_round = requests.post(url_round,data=json.dumps(payload_round))
            payload_round2 = {"round":round}
            response_round2 = requests.put(url_gamestarted,data=json.dumps(payload_round2))

            # Player1
            while True:
                movefeedback = playercanplay("player1",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition4:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (10,20):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player1"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    return
                elif movefeedback == "ok":
                    break

            # Player2
            while True:
                movefeedback = playercanplay("player2",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition1:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (40,50):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player2"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    return
                elif movefeedback == "ok":
                    break

            # Next round
            round += 1
            sleep(1)
            continue

    # 3 players
    elif players == "3":
        round = 1
        while True:

            # Start a new round
            payload_round = {"gameid":gameid,"round":str(round)}
            response_round = requests.post(url_round,data=json.dumps(payload_round))
            payload_round2 = {"round":round}
            response_round2 = requests.put(url_gamestarted,data=json.dumps(payload_round2))

            # Player1
            while True:
                movefeedback = playercanplay("player1",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition4:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (10,20):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player1"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    break
                elif movefeedback == "ok":
                    break

            # Player2
            while True:
                movefeedback = playercanplay("player2",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition6:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (30,40):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player2"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    break
                elif movefeedback == "ok":
                    break

            # Player3
            while True:
                movefeedback = playercanplay("player3",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition2:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (50,60):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player3"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    break
                elif movefeedback == "ok":
                    break

            # Next round
            round += 1
            sleep(1)
            continue

    # 4 players
    elif players == "4":
        round = 1
        while True:

            # Start a new round
            payload_round = {"gameid":gameid,"round":str(round)}
            response_round = requests.post(url_round,data=json.dumps(payload_round))
            payload_round2 = {"round":round}
            response_round2 = requests.put(url_gamestarted,data=json.dumps(payload_round2))

            # Player1
            while True:
                movefeedback = playercanplay("player1",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition4:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (10,20):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player1"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    break
                elif movefeedback == "ok":
                    break

            # Player2
            while True:
                movefeedback = playercanplay("player2",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition5:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (20,30):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player2"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    break
                elif movefeedback == "ok":
                    break

            # Player3
            while True:
                movefeedback = playercanplay("player3",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition1:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (40,50):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player3"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    break
                elif movefeedback == "ok":
                    break

            # Player4
            while True:
                movefeedback = playercanplay("player4",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition2:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (50,60):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player4"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    break
                elif movefeedback == "ok":
                    break

            # Next round
            round += 1
            sleep(1)
            continue

    # 6 players
    elif players == "6":
        round = 1
        while True:

            # Start a new round
            payload_round = {"gameid":gameid,"round":str(round)}
            response_round = requests.post(url_round,data=json.dumps(payload_round))
            payload_round2 = {"round":round}
            response_round2 = requests.put(url_gamestarted,data=json.dumps(payload_round2))

            # Player1
            while True:
                movefeedback = playercanplay("player1",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition4:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (10,20):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player1"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    break
                elif movefeedback == "ok":
                    break

            # Player2
            while True:
                movefeedback = playercanplay("player2",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition5:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (20,30):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player2"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    break
                elif movefeedback == "ok":
                    break

            # Player3
            while True:
                movefeedback = playercanplay("player3",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition6:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (30,40):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player3"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    break
                elif movefeedback == "ok":
                    break

            # Player4
            while True:
                movefeedback = playercanplay("player4",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition1:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (40,50):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player4"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    break
                elif movefeedback == "ok":
                    break

            # Player5
            while True:
                movefeedback = playercanplay("player5",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition2:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (50,60):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player5"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    break
                elif movefeedback == "ok":
                    break

            # Player6
            while True:
                movefeedback = playercanplay("player6",response_round.text,gameid)
                url_winnercheck = url + "/games?filter=id,eq," + gameid + "&transform=1"
                response_winnercheck = requests.get(url_winnercheck)
                response_winnercheck_json = response_winnercheck.json()
                score = 0
                for cnt_winner in startposition3:
                    if int(response_winnercheck_json["games"][0][cnt_winner]) in range (60,70):
                        score += 1
                if movefeedback == "ok" and score == 10:
                    url_setwinner = url + "/games/" + gameid
                    payload_setwinner = {"winner":response_winnercheck_json["games"][0]["player6"]}
                    response_setwinner = requests.put(url_setwinner,data=json.dumps(payload_setwinner))
                    break
                elif movefeedback == "ok":
                    break

            # Next round
            round += 1
            sleep(1)
            continue


# Check for games and start them
def game():
    while True:
        url_checknewgame = url + "/games?filter=started,ne,1&transform=1"
        response_checknewgame = requests.get(url_checknewgame)
        response_checknewgame_json = response_checknewgame.json()
        for cnt_games in response_checknewgame_json["games"]:

            # Start a game for 2 players
            if cnt_games["players"] == "2" and cnt_games["player1"] != "" and cnt_games["player2"] != "":
                create_startarea1(cnt_games["id"])
                create_startarea4(cnt_games["id"])
                gamestartthread = threading.Thread(target=game2, args=(cnt_games["players"],cnt_games["id"],))
                gamestartthread.start()
                #break

            # Start a game for 3 players
            elif cnt_games["players"] == "3" and cnt_games["player1"] != "" and cnt_games["player2"] != "" and cnt_games["player3"] != "":
                create_startarea1(cnt_games["id"])
                create_startarea3(cnt_games["id"])
                create_startarea5(cnt_games["id"])
                gamestartthread = threading.Thread(target=game2, args=(cnt_games["players"],cnt_games["id"],))
                gamestartthread.start()
                #break

            # Start a game for 4 players
            elif cnt_games["players"] == "4" and cnt_games["player1"] != "" and cnt_games["player2"] != "" and cnt_games["player3"] != "" and cnt_games["player4"] != "":
                create_startarea1(cnt_games["id"])
                create_startarea2(cnt_games["id"])
                create_startarea4(cnt_games["id"])
                create_startarea5(cnt_games["id"])
                gamestartthread = threading.Thread(target=game2, args=(cnt_games["players"],cnt_games["id"],))
                gamestartthread.start()
                #break

            # Start a ganme for 6 players
            elif cnt_games["players"] == "6" and cnt_games["player1"] != "" and cnt_games["player2"] != "" and cnt_games["player3"] != "" and cnt_games["player4"] != "" and cnt_games["player5"] != "" and cnt_games["player6"] != "":
                create_startarea1(cnt_games["id"])
                create_startarea2(cnt_games["id"])
                create_startarea3(cnt_games["id"])
                create_startarea4(cnt_games["id"])
                create_startarea5(cnt_games["id"])
                create_startarea6(cnt_games["id"])
                gamestartthread = threading.Thread(target=game2, args=(cnt_games["players"],cnt_games["id"],))
                gamestartthread.start()
                #break

            # Wait for games
            else:
                print("Waiting for games ...")

        else:
            sleep(1)
            continue

        break

game()

