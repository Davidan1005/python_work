from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages["Simon"] = "Spanish"
favourite_languages["Becky"] = " French"

for favourite_language in favourite_languages():
    print(favourite_language)