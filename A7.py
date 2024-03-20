"""
This program makes use of dictionaries to show the data of a bike-share network in Toronto and how it changes with
different actions without user input
Author: Martin Perez
Student Number: 20360377
Date: November 2022
"""


def initialize_bike_info():
    """
    This function defines the dictionary that will hold all the information.
    The dictionary is of the format:
        stationID (key): value is a dictionary
        So, for example an entry for station ID = 70 might look like:
            70: {"": "Jarvis", "cap": 50, "num_bikes": 4, "docks":2}
    A dictionary containing all the stations' info is returned.
    """
    station_id = {
        8010: {"location": "York", "cap": 31, "num_bikes": 20, "docks": 11},
        8011: {"location": "Esplanade", "cap": 15, "num_bikes": 5, "docks": 10},
        8012: {"location": "George", "cap": 19, "num_bikes": 1, "docks": 18},
        8013: {"location": "Madison", "cap": 15, "num_bikes": 2, "docks": 13},
        8014: {"location": "Elm", "cap": 11, "num_bikes": 0, "docks": 11},
        8015: {"location": "University", "cap": 19, "num_bikes": 1, "docks": 18},
        8016: {"location": "Bay", "cap": 11, "num_bikes": 11, "docks": 0},
        8017: {"location": "College", "cap": 11, "num_bikes": 1, "docks": 10},
    }
    return station_id


def change_info(bike_info, station_id, cap, num_bikes, docks):
    """
    This function changes the capacity, number of bikes available and the
    number of empty docks for the a given (id) station.
    Parameters:  bike_info - a dictionary
                 id - integer indicating the  id
                 cap - integer - number of bikes that the station accommodates
                 num_bikes - how many bikes are currently available for rent
                 docks - how many docs are currently free
    Returns:  Nothing returned, but bike_info is updated.
    """
    if station_id == station_id:
        bike_info[station_id]["cap"] = cap  # changes the capacity to what is given when the function is called
        bike_info[station_id]["num_bikes"] = num_bikes  # changes num_bikes to what is given when the function is called
        bike_info[station_id]["docks"] = docks  # the number of docks to what is given when the function is called


def bike_rental(bike_info, station_id):
    """
    Checks to ensure that stationID is a valid station in bike_info.
    If so, checks to see if there are bikes available at this station.
    If so, decrements the number of bikes available for rent at this station and increases
    the docks.
    Parameters: bike_info - a dictionary
                stationID -- integer representing the ID of the station from which to rent
    Returns:  True (bike was rented successfully), False (something went wrong)
              bike_info may be updated.
    """
    if int(station_id) > 8017 or int(station_id) < 8010:  # check for valid station info
        return False
    else:
        if int(bike_info[station_id]["num_bikes"]) == 0:  # check if a bike is available
            return False
        elif int(bike_info[station_id]["num_bikes"]) > 0:  # updates the dictionary if a bike is rented
            bike_info[station_id]["num_bikes"] = int(bike_info[station_id]["num_bikes"] - 1)
            bike_info[station_id]["docks"] = int(bike_info[station_id]["docks"] + 1)
            return True


def return_bike(bike_info, station_id):
    """
    Indicates whether or not a bike can be returned to the given station ID.
    Need to check if stationID is valid.  If not, return False (bike can't be returned here).
    A bike can be returned if there are available docks, otherwise it cannot be returned
    to that .
    Parameters:  bike_info - a dictionary
                 stationID - an integer
    Returns: True if a bike can be returned, False otherwise
    """
    if int(station_id) > 8017 or int(station_id) < 8010:  # check for valid station info
        return False
    else:
        if int(bike_info[station_id]["docks"]) == 0:  # check for available docks
            return False
        elif int(bike_info[station_id]["docks"]) > 0:  # updates dictionary if a dock is available
            bike_info[station_id]["docks"] = int(bike_info[station_id]["docks"] - 1)
            bike_info[station_id]["num_bikes"] = int(bike_info[station_id]["num_bikes"] + 1)
            return True


def get_info(bike_info, station_id):
    """
    This function looks up the information found at stationID in bike_info
    and returns the , capacity, bikes available and docks in a list.
    If stationID does not exist in bike_info, return an empty list.
    Parameters:  bike_info - a dictionary of the format {stationID: {values}}
                 stationId - integer
    Return: a list [, capacity, bikes_available, docks] or []
    """
    if int(station_id) > 8017 or int(station_id) < 8010:
        return []
    else:
        return [bike_info[station_id]["location"], bike_info[station_id]["cap"], bike_info[station_id]["num_bikes"],
                bike_info[station_id]["docks"]]


def docks_available(station_id):
    """
    This function returns the total number of docks available across all
    s.
    Parameters:  bike_info - a dictionary of the format {station_id: {values}}
    Return: integer
    """
    return int(
            (station_id[8010]["docks"]) + station_id[8011]["docks"] + station_id[8012]["docks"]
            + station_id[8013]["docks"] + station_id[8014]["docks"] + station_id[8015]["docks"]
            + station_id[8016]["docks"] + station_id[8017]["docks"]
    )


def test_code():
    # Test initialize function
    info = initialize_bike_info()
    print(info)
    print()

    # Test change info
    change_info(info, 8012, 15, 7, 8)
    print("After changing information for 8012, new info is:")
    print(info)

    # Test bike rental when bikes not available
    print("Number of bikes at 8014 before renting is", info[8014]["num_bikes"])
    bike_rental(info, 8014)
    print("Number of bikes at 8014 after renting is", info[8014]["num_bikes"])

    # Test bike rental when bikes  available
    print("Number of bikes at 8011 before renting is", info[8011]["num_bikes"])
    bike_rental(info, 8011)
    print("Number of bikes at 8011 after renting is", info[8011]["num_bikes"])
    print("Number of docks at 8011 after renting is", info[8011]["docks"])

    # Test information retrieval for a specific  that doesn't exist
    stat_info = get_info(info, 1010)
    if len(stat_info) == 0:
        print("Station does not exist")
    else:
        print("Info for station 1010 is ", stat_info)

    # Test information retrieval for a specific  that exists
    stat_info = get_info(info, 8010)
    if len(stat_info) == 0:
        print("Station does not exist")
    else:
        print("Info for station 8010 is ", stat_info)

    # Test to find total number of docks available
    print("Total number of docks available: ", docks_available(info))

    # Test bike return - run through all cases
    for key in info:
        if return_bike(info, key):
            print("Returned bike successfully to ", key)
        else:
            print("Could not return bike to", key)


test_code()
