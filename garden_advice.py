def get_user_input():
    """Prompt user for season and plant type"""
    season = input("Enter the season (winter/spring/summer/fall): ").lower()
    plant_type = input("Enter the plant type: ").lower()
    return season, plant_type


def get_season_advice(season):
    """Return advice based on the season"""
    if season == "summer":
        return "Water your plants regularly; provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers\n"
    elif season == "fall":
        return "Keep you plants hydrated and prepare for winter\n"
    elif season == "spring":
        return "Keep an eye on your plants, this is their favorite time of year!\n"
    else:
        return "No advice for this season\n"


def get_plant_advice(plant_type):
    """Return advice based on the plant type"""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms"
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant"


def main():
    """Main function to run the gardening app."""
    season, plant_type = get_user_input()

    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type)

    print("\nGardening Advice:")
    print(advice)


# Run the program
if __name__ == "__main__":
    main()