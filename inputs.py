### Configures the inputs for a given letters patent.

####################
# UNIVERSAL INPUTS #
####################

# "peerage" indicates a patent granting a peerage or baronetage. "other"
# indicates a miscelleneous type of patent.
patent_type = "peerage"

ramno = 1731

day = 3
# Write out the month's name in full.
month = "Primilis"
year = 1

#######################
# PEERAGE-ONLY INPUTS #
#######################

# If the letters patent are NOT for a peerage, leave well alone.

grantee = "John Smith"
# Either "male" of "female" - no non-binary nonsense!
gender = "male"
# Either "duke", "marquess", "earl", "viscount", "baron" or "baronet".
degree = "earl"
title = "Earl of Somewhere"
# Use a list type. The order here is the order in which they'll appear on
# the letters patent.
subsidiary_titles = ["Viscount Smith"]
# Should begin with "Whereas" and end with a comma.
whereas = "Whereas one John Smith has proved to be a good egg,"
# Enter either a code for a standard remainder, or the custom remainder in
# full, beginning with "and" and ending without punctuation.
remainder = "perpetual"

#####################
# OTHER-ONLY INPUTS #
#####################

# If the letters patent are NOT of "other" type, leave well alone.

filling = "Filling!"
