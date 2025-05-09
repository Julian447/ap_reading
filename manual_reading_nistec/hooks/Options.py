# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
import json


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class GenerateChapters(Range):
    num = 10
    for i in range(num-1):
        item = {"count": {i},"name": "Progressive Chapter","category": ["Chapters"],"filler": True}
        location = {"name": f"Chapter {i}", "category": ["Chapters"],"requires": [f"Chapter {i-1}"]}

        with open('../data/items.json', 'r+') as f:
            data = json.load(f)
            data.append(item)
            json.dump(data, f, indent=4)
            f.truncate()
        with open('../data/locations.json', 'r+') as f:
            data = json.load(f)
            data.append(location)
            json.dump(data, f, indent=4)
            f.truncate()


    item = {"count": 1,"name": "Last Chapter","category": ["Chapters"],"filler": True}

    location = {"name": "Last Chapter", "category": ["Chapters"],"requires": [f"Chapter {num-1}"]}

    with open('../data/items.json', 'r+') as f:
        data = json.load(f)
        data.append(item)
        json.dump(data, f, indent=4)
        f.truncate()
    with open('../data/locations.json', 'r+') as f:
        data = json.load(f)
        data.append(location)
        json.dump(data, f, indent=4)
        f.truncate()

class TotalCharactersToWinWith(Range):
    """Instead of having to beat the game with all characters, you can limit locations to a subset of character victory locations."""
    display_name = "Number of characters to beat the game with before victory"
    range_start = 10
    range_end = 50
    default = 50


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["num_chapters"] = GenerateChapters
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options
