teams_dictionary={
	1678:{
		"Location":"Davis_CA",
		"Rookie_year":2005, 
		"2019_Competition_Status":True, 
		"Names_of_Competions":[
			"Central_Valley_Regional", 
			"Sacramento_Regional", 
			"Aerospace_Valley_Regional",
			"Carver_Division",
			"Einstein_Field",
			"RCC_Qianjiang_International_Robotics_Invitational",
			"Chezy_Champs"], 
		"Competition_Location":[
			"Fresno_CA",
			"Davis_CA", 
			"Lancaster_CA",
			"Houston_TX",
			"Houston_TX",
			"Hangzhou_CN",
			"San_Jose_CA"], 
		"Competition_Awards":[
			"Regional_Chairmans_Award", 
			"Regional_Winner",
			"Deans_List",
			"Regional_Winner",
			"Industrial_Design_Award",
			"Excellence_in_Engineering",
			"Championship_Subdivision_Winner",
			"Entrepreneurship-Award"]},
	3132:{
		"Location":"Sydney_Australia",
		"Rookie_year":2010,
		"2019_Competition_Status":True,
		"Names_of_Competions":[
			"Southern_Cross_Regional",
			"South_Pacific_Regional",
			"Carver_Division",
			"Einstein_Field"],
		"Competition_Location":[
			"Sydeny_Olympic_Park",
			"Sydeny_Olympic_Park",
			"Houston_TX",
			"Houston_TX"],
		"Competition_Awards":[
			"Woodie_Flowers",
			"Gracious_Professionalism",
			"Regional_Engineering_Inspiration",
			"Safety_Award"]},
	1902:{
		"Location":"Orlando_FL",
		"Rookie_year":2006, 
		"2019_Competition_Status":True, 
		"Names_of_Competions":[
			"Palmetto_Regional", 
			"Orlando_Regional", 
			"Newton_Division",
			"Einstein_Field"], 
		"Competition_Location":[
			"Myrtle_Beach",
			"Orlando_FL", 
			"Houston_TX",
			"Houston_TX"], 
		"Competition_Awards":[
			"Regional_Chairmans_Award", 
			"Deans_List",
			"Entrepreneurship-Award",
			"Chairmans_Award_Finalist"]},
	5458:{
		"Location":"Woodland_CA",
		"Rookie_year":2015,
		"2019_Competition_Status":True,
		"Names_of_Competions":[
			"Central_Valley_Regional",
			"Sacramento_Regional"],
		"Competition_Location":[
			"Fresno_CA",
			"Davis_CA"],
		"Competition_Awards":[
			"None"]},
	6174:{
		"Location":"Winters_CA",
		"Rookie_year":2016,
		"2019_Competition_Status":True,
		"Names_of_Competions":[
			"Sacramento_Regional"],
		"Competition_Location":[
			"Davis_CA"],
		"Competition_Awards":[
			"None"]}}
team_number = int(input("Out of 1678, 3132, 1902, 5458, and 6174, what is the number of the desired team?"))
team_attribute = str(input(
	"""Out of:
	Location, 
	Rookie_year, 
	2019_Competition_Status, 
	Names_of_Competitions, 
	Competition_Locations, 
	Competition_Awards 
	what is the desired attribute?"""))
print(teams_dictionary[team_number][team_attribute])