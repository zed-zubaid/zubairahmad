# zubair ahmad




from math import floor, inf


# File names
RACE_FILE    = "Races.txt"
RUNNERS_FILE = "Runners.txt"

# races :: Race Name -> [race]
# race is just a list of: (Runner code :: String, Time :: Int (seconds))
races   = {}
# runners :: Runner name -> Runner code
runners = {}


###############
# Aux Functions
###############

def fst(xs):

    # Returns the first element of a container

    return xs[0]

def snd(xs):

    # Returns the second element of a container

    return xs[1]

def stringLen(x):

    # Finds the length of a string representable object

    return len(str(x))


def find_maximum_width(ss):

    return max(map(stringLen,ss) )

def readRaces():

    with open(RACE_FILE,"r") as f:
        for line in f:
            # races["Currabiny"]    = []
            # races["Glengarrifff"] = []
            line        = line.replace("\n","")
            races[line] = []

def readRunners():

    # Initializes the runners variable, each runner name is associated with
    # the corresponding runners code.

    with open(RUNNERS_FILE,"r") as f:
        for line in f:
            #(name,code)
            #(name,code)  = tuple(line)
            (name,code)   = line.split(",")
            code          = code.replace("\n","")
            # runners["Anna Fox"] = "CK-24"
            runners[name] = code

def readVenue(file_name,info):

    with open(file_name,"r") as f:
        for line in f:
            (code,time) = line.split(",")
            info.append((code,int(time)))



def toTime(total_seconds):
   
    # Given a quantity in seconds, transform it into a tuple of: (minutes,seconds).
    # toTime(3600) == (60,0)
    # toTime(125)  == (2,5)

    minutes = floor(total_seconds / 60)
    seconds = total_seconds % 60
    #      (something, something else)
    return (minutes,seconds)

def getWinner(Venue):
  
    # Gets the winner code of a specific Venue.

    results    = races[Venue]
    codes      = list(map(fst,results))
    total_time = list(map(snd,results))

    # dummy value in order to begin comparisons.
    winner_so_far = ("",inf)
    # ("CK-24",3040) < ("",inf)
    # winner_so_far = ("CK-24",3040)
    # ("KY-43",2915) < ("CK-24",3040) 
    # winner_so_far = ("KY-43",2915)
    for (code,time) in zip(codes,total_time):
        if time < winner_so_far[1]:
            winner_so_far = (code,time)

    return winner_so_far[0]



def show_by_county(county_name,county_code):

    # Shows all competitors of a specific county.
    # county_name :: String, The (full) name of the county
    # county_code :: String, The code (in format: XY) of the county


    print(f"{county_name} runners")
    print("-"*12)
    
    maximum_name_width = find_maximum_width(runners.keys())
    for runner_name in runners:
        if county_code in runners[runner_name]:
            print(f"\t{runner_name:<{maximum_name_width}}\t{runners[runner_name]}")

def cls():

    # Clears the screen printing 100 line breaks

    print("\n"*100)


def show_races_competitor_venue(runner_code,venue):

    # Given a runner code and a venue, prints the result of the runner in the race.

    results    = races[venue]
    codes      = list(map(fst,results))
    total_time = list(map(snd,results))

    if runner_code not in codes:
        return

                        # [(CK-24,time)] -> (CK-24,time) -> time
    runner_time       = [code for code in results if code[0] == runner_code][0][1]
    runner_time_tuple = toTime(runner_time)
    runner_time_mins  = runner_time_tuple[0]
    runner_time_secs  = runner_time_tuple[1]
    pos           = 0
    total_runners = 0
    for (code,time) in zip(codes,total_time):
        if (runner_code != code) and (runner_time > time):
            pos += 1
        total_runners += 1
    
    print(f"{venue}\t{runner_time_mins} mins {runner_time_secs} secs ({pos+1} of {total_runners})")
    
    


def show_races_competitor(runner_name):
    """
    wrapper for show_races_competitor_venue
    """
    runner_code = runners[runner_name]
    print(f"{runner_name} ({runner_code})")
    print("-"*40)
    for venue in races:
        show_races_competitor_venue(runner_code,venue)

##################
## Main Functions
##################

def readFiles():

    readRaces()
    readRunners()
    for key in races:
        
        readVenue(key + ".txt",races[key])


def show_all_by_county():

    # Shows all competitors by county

    show_by_county("Cork","CK")
    show_by_county("Kerry","KY")

    input()


def show_winners():

    # Shows the winner for each race.

    maximum_race_width = find_maximum_width(races.keys())
    aux = "Venue"
    print(f"{aux:<{maximum_race_width}}\tWinner")
    print("="*23)
    for race in races:
        winner = getWinner(race)
        print(f"{race:<{maximum_race_width}}\t{winner}")
    
    input()

def show_won_race():

    # Show all comptetitors that have won a race.
  
    print("The following runners have all won at least one race:")
    print("-----------------------------------------------------")
    aux = {}
    for runner in runners:
        # runner = "Anna Fox"
        # runners["Anna Fox"] = "CK-24"
        # aux["CK-24"] = "Anna Fox"
        aux[runners[runner]] = runner

    maximum_name_width = find_maximum_width(runners.keys())
    for race in races:
        winner_code = getWinner(race)
        winner_name = aux[winner_code]
        print(f"{winner_name:<{maximum_name_width}}\t ({winner_code})")
    
    input()

def show_results_for_race():
 
    total_races = len(races)
    aux = {}
    # range(1,total_races+1) = (1,2)
    # races = "Currabinny", "Glengarrriff"
    # zip(range(1,total_races+1),races) = [(1,"Currabinny"), (2,"Glengarrriff")]
    # 1: Currabinny
    # 2: Glengarriff
    # aux = "1": "Currabinny"
    #       "2": "Glengarriff"
    for (i,race) in zip(range(1,total_races+1),races):
        print(f"{i}: {race}")
        aux[str(i)] = race
    choice = input("Choice > ")

    if choice not in aux:
        print("Please input a valid number.")
        input()
        cls()
        show_results_for_race()
        return

    input()

def show_one_competitor():
    total_runners = len(runners.keys())
    aux = {}
    for (i,runner_name) in zip(range(1,total_runners+1), runners):
        print(f"{i}: {runner_name}")
        aux[str(i)] = runner_name
    choice = input("Which runner > ")
    if choice not in aux:
        print("Please input a valid choice.")
        input()
        cls()
        show_one_competitor()
        return ()
    
    print("\n")
    show_races_competitor(aux[choice])
    input()


main_menu = (
    {
        "1":show_results_for_race,
        "2":show_all_by_county,
        "3":show_winners,
        "4":show_one_competitor,
        "5":show_won_race,
        "6":quit
    }
)

def main():
    readFiles()

    while(True):
        cls()
        print("1. Show the results for a race")
        print("2. Show all competitors by county")
        print("3. Show the winner of each race")
        print("4. Show all the race times for one competitor")
        print("5. Show all competitors who have won a race")
        print("6. Quit")
        print("\n")
        choice = input("Choice > ")
        if choice not in main_menu:
            print("Invalid option, try again")
            input()
            cls()
            continue
        main_menu[choice]()

main()