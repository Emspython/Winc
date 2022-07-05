# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

# Variables
Language_Spain = 'Spanish'
Language_Switzerland = 'Swiss'
Common_Religion_Spain = 'Roman Catholic'
Common_Religion_Switzerland = 'Roman Catholic'
Capital_Spain = 'Madrid'
Capital_Switzerland = 'Bern'
Spain_GDP = 1714860000000
Switzerland_GDP = 590710000000
Pop_growth_Spain = '1,95%'
Pop_growth_Switzerland = '0,65%'
Pop_count_Spain = 47163418
Pop_count_Switzerland = 85086980

# Vergelijkingen

#1 The language spoken the most in Switzerland is the same as in Spain.
Com_Language = Language_Spain == Language_Switzerland
#2 The most prevalent religion in Switzerland is the same as in Spain.
Prev_Religion = Common_Religion_Spain == Common_Religion_Switzerland
#3 The name length of Spain's capital does not equal that of Switzerland.
Lenght_Capital = (len(Capital_Spain))!= len(Capital_Switzerland)
#4 Switzerland's GDP is greater than Spain's GDP.
Switzerland_GDP_Bigger_Than = Switzerland_GDP > Spain_GDP
#5 The population growth is less than 1% in Switzerland and Spain.
Tot_Growth_Spain = Pop_growth_Spain < '1%'
Tot_Growth_Switzerland = Pop_growth_Switzerland <'1%'
Tot_Growth = Pop_growth_Spain and Pop_growth_Switzerland <'1%'
#6 The population growth is less than 1% in Switzerland and Spain.
Pop_10mill_Spain = Pop_count_Spain > 10000000
Pop_10mill_Switzerland = Pop_count_Switzerland > 10000000
Population = Pop_count_Spain > 10000000 or Pop_count_Switzerland >= 10000000
#7 Exactly one of the two countries has a population count of over 10 million.
Pop_over_10mil = Pop_count_Spain and Pop_count_Switzerland > 10000000

# Print resultaten
print(Com_Language)
print(Prev_Religion)
print(Lenght_Capital)
print(Switzerland_GDP_Bigger_Than)
print(Tot_Growth)
print(Population)
print(Pop_over_10mil)




