
# No other modules apart from 'socket', 'BeautifulSoup', 'requests' and 'datetime'
# need to be imported as they aren't required to solve the assignment

# Import required module/s
import socket
from bs4 import BeautifulSoup
import requests
import datetime


# Define constants for IP and Port address of Server
# NOTE: DO NOT modify the values of these two constants
HOST = '127.0.0.1'
PORT = 24680


def fetchWebsiteData(url_website):
	"""Fetches rows of tabular data from given URL of a website with data excluding table headers.

	Parameters
	----------
	url_website : str
		URL of a website

	Returns
	-------
	bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""
	
	web_page_data = ''

	##############	ADD YOUR CODE HERE	##############
	req = requests.get(url_website)
	soup = BeautifulSoup(req.text, 'html.parser')
	body = soup.find('tbody')
	web_page_data = body.find_all('tr')
	##################################################

	return web_page_data


def fetchVaccineDoses(web_page_data):
	"""Fetch the Vaccine Doses available from the Web-page data and provide Options to select the respective Dose.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers

	Returns
	-------
	dict
		Dictionary with the Doses available and Options to select, with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineDoses(web_page_data))
	{'1': 'Dose 1', '2': 'Dose 2'}
	"""

	vaccine_doses_dict = {}

	##############	ADD YOUR CODE HERE	##############
	val = '1'
	check=[]
	for r in web_page_data:
		var = r.find('td',class_ = 'dose_num').text
		st = "Dose " + var
		if st not in check:
			check.append(st)
	check.sort()
	for doses in check:
		vaccine_doses_dict[val] = doses
		val = str(int(val)+1)
	#print(vaccine_doses_dict)

	##################################################

	return vaccine_doses_dict


def fetchAgeGroup(web_page_data, dose):
	"""Fetch the Age Groups for whom Vaccination is available from the Web-page data for a given Dose
	and provide Options to select the respective Age Group.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Age Groups (for whom Vaccination is available for a given Dose) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchAgeGroup(web_page_data, '1'))
	{'1': '18+', '2': '45+'}
	>>> print(fetchAgeGroup(web_page_data, '2'))
	{'1': '18+', '2': '45+'}
	"""

	age_group_dict = {}

	##############	ADD YOUR CODE HERE	##############
	var = '1'
	check = []
	
	for r in web_page_data:
		a = r.find('td',class_='dose_num').text
		b = r.find('td',class_='age').text
		if(a == dose and b not in check):
			check.append(b)
	check.sort()
	for val in check:
		age_group_dict[var] = val
		var = str(int(var)+1)

	

	##################################################

	return age_group_dict


def fetchStates(web_page_data, age_group, dose):
	"""Fetch the States where Vaccination is available from the Web-page data for a given Dose and Age Group
	and provide Options to select the respective State.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the States (where the Vaccination is available for a given Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchStates(web_page_data, '18+', '1'))
	{
		'1': 'Andhra Pradesh', '2': 'Arunachal Pradesh', '3': 'Bihar', '4': 'Chandigarh', '5': 'Delhi', '6': 'Goa',
		'7': 'Gujarat', '8': 'Harayana', '9': 'Himachal Pradesh', '10': 'Jammu and Kashmir', '11': 'Kerala', '12': 'Telangana'
	}
	"""

	states_dict = {}

	##############	ADD YOUR CODE HERE	##############
	var = '1'
	check = []
	
	for r in web_page_data:
		a = r.find('td',class_='dose_num').text
		b = r.find('td',class_='age').text
		c = r.find('td',class_='state_name').text
		if(a == dose and b == age_group and c not in check):
			check.append(c)
	check.sort()
	for val in check:
		states_dict[var] = val
		var = str(int(var)+1)

	##################################################

	return states_dict


def fetchDistricts(web_page_data, state, age_group, dose):
	"""Fetch the District where Vaccination is available from the Web-page data for a given State, Dose and Age Group
	and provide Options to select the respective District.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Districts (where the Vaccination is available for a given State, Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchDistricts(web_page_data, 'Ladakh', '18+', '2'))
	{
		'1': 'Kargil', '2': 'Leh'
	}
	"""

	districts_dict = {}

	##############	ADD YOUR CODE HERE	##############
	

	var = '1'
	check = []
	
	for r in web_page_data:
		a = r.find('td',class_='dose_num').text
		b = r.find('td',class_='age').text
		c = r.find('td',class_='state_name').text
		d = r.find('td',class_='district_name').text
		if(a == dose and b == age_group and c == state and d not in check):
			check.append(d)
	check.sort()
	for val in check:
		districts_dict[var] = val
		var = str(int(var)+1)
	##################################################

	return districts_dict


def fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose):
	"""Fetch the Hospital and the Vaccine Names from the Web-page data available for a given District, State, Dose and Age Group
	and provide Options to select the respective Hospital and Vaccine Name.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Hosptial and Vaccine Names (where the Vaccination is available for a given District, State, Dose, Age Group)
		and Options to select, with Key as 'Option' and Value as another dictionary having Key as 'Hospital Name' and Value as 'Vaccine Name'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchHospitalVaccineNames(web_page_data, 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {
				'MedStar Hospital Center': 'Covaxin'
			}
	}
	>>> print(fetchHospitalVaccineNames(web_page_data, 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {
				'Eden Clinic': 'Covishield'
			}
	}
	"""
	
	hospital_vaccine_names_dict = {}

	##############	ADD YOUR CODE HERE	##############
	var = '1'
	check = []
	
	for r in web_page_data:
		a = r.find('td',class_='dose_num').text
		b = r.find('td',class_='age').text
		c = r.find('td',class_='state_name').text
		d = r.find('td',class_='district_name').text
		e = r.find('td',class_='hospital_name').text
		f = r.find('td',class_='vaccine_name').text
		d1 = {}
		if(a == dose and b == age_group and c == state and d == district and e not in check):
			d1[e] = f
			check.append(d1)
	check.sort()
	for val in check:
		hospital_vaccine_names_dict[var] = val
		var = str(int(var)+1)	

	##################################################

	return hospital_vaccine_names_dict


def fetchVaccineSlots(web_page_data, hospital_name, district, state, age_group, dose):
	"""Fetch the Dates and Slots available on those dates from the Web-page data available for a given Hospital Name, District, State, Dose and Age Group
	and provide Options to select the respective Date and available Slots.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	hospital_name : str
		Name of Hospital where Vaccination is available for given District, State, Dose and Age Group
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Dates and Slots available on those dates (where the Vaccination is available for a given Hospital Name,
		District, State, Dose, Age Group) and Options to select, with Key as 'Option' and Value as another dictionary having
		Key as 'Date' and Value as 'Available Slots'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineSlots(web_page_data, 'MedStar Hospital Center', 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '81'}, '3': {'May 17': '109'}, '4': {'May 18': '78'},
		'5': {'May 19': '89'}, '6': {'May 20': '57'}, '7': {'May 21': '77'}
	}
	>>> print(fetchVaccineSlots(web_page_data, 'Eden Clinic', 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '137'}, '3': {'May 17': '50'}, '4': {'May 18': '78'},
		'5': {'May 19': '145'}, '6': {'May 20': '64'}, '7': {'May 21': '57'}
	}
	"""

	vaccine_slots = {}

	##############	ADD YOUR CODE HERE	##############
	
	for r in web_page_data:
		a = r.find('td',class_='dose_num').text
		b = r.find('td',class_='age').text
		c = r.find('td',class_='state_name').text
		d = r.find('td',class_='district_name').text
		e = r.find('td',class_='hospital_name').text
		f = r.find('td',class_='vaccine_name').text
		d1 = {}
		var = '1'
		if(a == dose and b == age_group and c == state and d == district and e == hospital_name):
			m1 = r.find('td',class_='may_15').text
			m2 = r.find('td',class_='may_16').text
			m3 = r.find('td',class_='may_17').text
			m4 = r.find('td',class_='may_18').text
			m5 = r.find('td',class_='may_19').text
			m6 = r.find('td',class_='may_20').text
			m7 = r.find('td',class_='may_21').text
			vaccine_slots[var] = {'May 15':m1}
			var = str(int(var)+1)
			vaccine_slots[var] = {'May 16':m2}
			var = str(int(var)+1)
			vaccine_slots[var] = {'May 17':m3}
			var = str(int(var)+1)
			vaccine_slots[var] = {'May 18':m4}
			var = str(int(var)+1)
			vaccine_slots[var] = {'May 19':m5}
			var = str(int(var)+1)
			vaccine_slots[var] = {'May 20':m6}
			var = str(int(var)+1)
			vaccine_slots[var] = {'May 21':m7}
			var = str(int(var)+1)

	##################################################

	return vaccine_slots


def openConnection():
	"""Opens a socket connection on the HOST with the PORT address.

	Returns
	-------
	socket
		Object of socket class for the Client connected to Server and communicate further with it
	tuple
		IP and Port address of the Client connected to Server
	"""

	client_socket = None
	client_addr = None

	##############	ADD YOUR CODE HERE	##############
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((HOST,PORT))
	s.listen(1)
	client_socket,client_addr = s.accept()
	print(f'Client is connected at: %s'%(client_addr,))
	##################################################
	
	return client_socket, client_addr


def startCommunication(client_conn, client_addr, web_page_data):
	"""Starts the communication channel with the connected Client for scheduling an Appointment for Vaccination.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	client_addr : tuple
		IP and Port address of the Client connected to Server
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""

	##############	ADD YOUR CODE HERE	##############
	#invalid = 0
	msg = '============================\n# Welcome to CoWIN ChatBot #\n============================\n\nSchedule an Appointment for Vaccination:\n'
	client_conn.send(msg.encode())
	selectdose(client_conn)
	##################################################


def stopCommunication(client_conn):
	"""Stops or Closes the communication channel of the Client with a message.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	"""

	##############	ADD YOUR CODE HERE	##############
	msg = '\n<<< See ya! Visit again :)'
	client_conn.send(msg.encode())
	client_conn.close()

	##################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################
invalid = 0
invalidage = 0
invalidstate = 0
invalid_dist = 0
def dateinput(dose):# function for checking validity of input date as well as scheduling of 2nd dose
	datein = client_conn.recv(1024).decode('utf-8')
	if(datein == 'b' or datein == 'B'):# option to go back to previous state of flowchart
		selectdose(client_conn)
	elif(datein == 'q' or datein == 'Q'):#option for user to quit the program voluntarily
		print("Client wants to quit!")
		print("Saying Bye to client and closing the connection!")
		stopCommunication(client_conn)
	else:
		today = datetime.date.today()
		try:
	 		dateob = datetime.datetime.strptime(datein,"%d/%m/%Y").date()
		except ValueError:#if user enters date in wrong format display following message and recall
			m3 = "\n<<< Invalid Date provided of First Vaccination Dose: "+str(datein)
			m3 = m3+"\n>>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g 12/5/2021"
			client_conn.send(m3.encode())
			dateinput(dose)
		else:	
			#today = datetime.date.today()
			#datein = datetime.date(year,month,day)
			#start = datetime.date(2021,5,15)
			#end = datetime.date(2021,5,21)
			if (today >= dateob):
				weeks = ((today - dateob).days)//7
				m3 = "\n<<< Date of First Vaccination Dose provided: "+str(datein)
				m3 = m3 + "\n<<< Number of weeks from today: "+str(weeks)
				client_conn.send(m3.encode())
				if weeks >=4 and weeks <=8:
					m3 = "\n<<< You are eligible for 2nd Vaccination Dose and are in the right time-frame to take it."
					client_conn.send(m3.encode())
					selectage(dose,client_conn)
				elif weeks <= 4:
					m3 = "\n<<< You are not eligible right now for 2nd Vaccination Dose! Try after "+str(4 - weeks)+" weeks."
					client_conn.send(m3.encode())
					stopCommunication(client_conn)
				elif weeks >=8:
					m3 = "\n<<< You have been late in scheduling your 2nd Vaccination Dose by "+str(weeks - 8)+" weeks."
					client_conn.send(m3.encode())
					selectage(dose,client_conn)
			else:
				m3 = "\n<<< Invalid Date provided of First Vaccination Dose: "+str(datein)
				m3 = m3+"\n>>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g 12/5/2021"
				client_conn.send(m3.encode())
				dateinput(dose)



def selectdose(client_conn):#function for checking the dose value and moving accordingly on the flowchart
	global invalid
	msg = "\n>>> Select the Dose of Vaccination:\n"+str(fetchVaccineDoses(web_page_data))
	client_conn.send(msg.encode())
	dose = client_conn.recv(1024).decode('utf-8')#recieving dose input from user
	if fetchVaccineDoses(web_page_data).get(dose) or dose=='b' or dose =='B' or dose == 'q' or dose == 'Q':
		m2 = "\n<<< Dose selected: " + str(dose)
		if dose == '1':
			client_conn.send(m2.encode())
			print("Dose selected:  %s"%dose)
			selectage(dose,client_conn)
		elif dose == 'b' or dose == 'B':# option to go back to previous state of flowchart
			selectdose(client_conn)
		elif dose == 'q' or dose == 'Q':#option for user to quit the program voluntarily
			print("Client wants to quit!")
			print("Saying Bye to client and closing the connection!")
			stopCommunication(client_conn)
		else:
			m2 = m2 + "\n>>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g 12/5/2021"
			client_conn.send(m2.encode())
			print("Dose selected:  %s"%dose)
			dateinput(dose)
	else:
		if invalid == 3:#checking count of invalid input by the user
			stopCommunication(client_conn)
		else:
			invalid = invalid + 1
			m2 = "\n<<< Invalid input provided "+str(invalid)+" time(s)! Try again."
			client_conn.send(m2.encode())
			if invalid == 3:
				stopCommunication(client_conn)#closing the program upon 3 invalid inputs
			else:
				selectdose(client_conn)


def selectage(dose,client_conn):#function for providing user with valid age group options
	global invalid
	msg = "\n>>> Select the Age Group:\n"+str(fetchAgeGroup(web_page_data, dose))
	client_conn.send(msg.encode())
	age = client_conn.recv(1024).decode('utf-8')#recieving age input from user
	if (fetchAgeGroup(web_page_data, dose).get(age) or (age=='b' or age =='B' or age == 'q' or age == 'Q')):
		if age == 'b' or age == 'B':# option to go back to previous state of flowchart
			selectdose(client_conn)
		elif age == 'q' or age == 'Q':#option for user to quit the program voluntarily
			print("Client wants to quit!")
			print("Saying Bye to client and closing the connection!")
			stopCommunication(client_conn)
		else:
			age_group = str(fetchAgeGroup(web_page_data, dose).get(age))
			m2 = "\n<<< Selected Age Group: "+str(fetchAgeGroup(web_page_data, dose).get(age))
			client_conn.send(m2.encode())
			print("Age Group selected:  %s"%age_group)
			selectstate(age_group,dose,client_conn)
	else:
		if invalid == 3:
			stopCommunication(client_conn)
		else:
			invalid = invalid + 1
			m2 = "\n<<< Invalid input provided "+str(invalid)+" time(s)! Try again."
			client_conn.send(m2.encode())
			if invalid== 3:
				stopCommunication(client_conn)
			else:
				selectage(dose,client_conn)


def selectstate(age_group,dose,client_conn):#function for providing user with valid state options for given dose and age.
	global invalid
	msg = "\n>>> Select the State:\n"+str(fetchStates(web_page_data, age_group, dose))
	client_conn.send(msg.encode())
	state = client_conn.recv(1024).decode('utf-8')#recieve user input about state selection
	if (fetchStates(web_page_data,age_group,dose).get(state) or (state=='b' or state =='B' or state == 'q' or state == 'Q')):
		if state == 'b' or state == 'B':# option to go back to previous state of flowchart
			selectage(dose,client_conn)
		elif state == 'q' or state == 'Q':#option for user to quit the program voluntarily
			print("Client wants to quit!")
			print("Saying Bye to client and closing the connection!")
			stopCommunication(client_conn)
		else:
			state_name = str(fetchStates(web_page_data, age_group, dose).get(state))
			m2 = "\n<<< Selected State: "+state_name+"\n"
			client_conn.send(m2.encode())
			print("State selected:  %s" %state_name)
			selectdist(age_group,dose,state_name,client_conn)
	else:
		if invalid == 3:
			stopCommunication(client_conn)
		else:
			invalid = invalid + 1
			m2 = "\n<<< Invalid input provided "+str(invalid)+" time(s)! Try again."
			client_conn.send(m2.encode())
			if invalid == 3:
				stopCommunication(client_conn)
			else:
				selectstate(age_group,dose,client_conn)

def selectdist(age_group,dose,state_name,client_conn):#function for providing user with available districts for chosen state.
	global invalid
	msg = "\n>>> Select the District:\n"+str(fetchDistricts(web_page_data, state_name, age_group, dose))
	client_conn.send(msg.encode())
	dist = client_conn.recv(1024).decode('utf-8')#user input
	if (fetchDistricts(web_page_data, state_name, age_group, dose).get(dist) or (dist=='b' or dist =='B' or dist == 'q' or dist == 'Q')):
		if dist == 'b' or dist == 'B':# option to go back to previous state of flowchart
			selectstate(age_group,dose,client_conn)
		elif dist == 'q' or dist == 'Q':#option for user to quit the program voluntarily
			print("Client wants to quit!")
			print("Saying Bye to client and closing the connection!")
			stopCommunication(client_conn)
		else:
			dist_name = str(fetchDistricts(web_page_data, state_name, age_group, dose).get(dist))
			m2 = "\n<<< Selected District: "+dist_name+"\n"
			client_conn.send(m2.encode())
			print("District selected:  %s" %dist_name)
			selecthosp(age_group,dose,state_name,dist_name,client_conn)
	else:
		if invalid == 3:
			stopCommunication(client_conn)
		else:
			invalid = invalid + 1
			m2 = "\n<<< Invalid input provided "+str(invalid)+" time(s)! Try again."
			client_conn.send(m2.encode())
			if invalid == 3:
				stopCommunication(client_conn)
			else:
				selectdist(age_group,dose,state_name,client_conn)

def selecthosp(age_group,dose,state_name,dist_name,client_conn):
	global invalid
	msg = "\n>>> Select the Vaccination Center Name:\n"+str(fetchHospitalVaccineNames(web_page_data, dist_name, state_name, age_group, dose))
	client_conn.send(msg.encode())
	hosp = client_conn.recv(1024).decode('utf-8')
	if (fetchHospitalVaccineNames(web_page_data, dist_name, state_name, age_group, dose).get(hosp) or (hosp=='b' or hosp =='B' or hosp == 'q' or hosp == 'Q')):
		if hosp == 'b' or hosp == 'B':# option to go back to previous state of flowchart
			selectdist(age_group,dose,state_name,client_conn)
		elif hosp == 'q' or hosp == 'Q':#option for user to quit the program voluntarily
			print("Client wants to quit!")
			print("Saying Bye to client and closing the connection!")
			stopCommunication(client_conn)
		else:
			dic = (fetchHospitalVaccineNames(web_page_data, dist_name, state_name, age_group, dose).get(hosp))
			hos = list(dic.keys())[0]
			m2 = "\n<<< Selected Vaccination Center: "+str(hos)
			client_conn.send(m2.encode())
			print("Hospital selected:  %s" %hos)
			selectslot(age_group,dose,state_name,dist_name,hos,client_conn)
	else:
		if invalid == 3:
			stopCommunication(client_conn)
		else:
			invalid = invalid + 1
			m2 = "\n<<< Invalid input provided "+str(invalid)+" time(s)! Try again."
			client_conn.send(m2.encode())
			if invalid == 3:
				stopCommunication(client_conn)
			else:
				selecthosp(age_group,dose,state_name,dist_name,client_conn)

def selectslot(age_group,dose,state_name,dist_name,hos,client_conn):
	global invalid
	msg = "\n>>> Select one of the available slots to schedule the Appointment:\n"+str(fetchVaccineSlots(web_page_data, hos, dist_name, state_name, age_group, dose))
	client_conn.send(msg.encode())
	slot = client_conn.recv(1024).decode('utf-8')
	if (fetchVaccineSlots(web_page_data, hos, dist_name, state_name, age_group, dose).get(slot) or (slot=='b' or slot =='B' or slot == 'q' or slot == 'Q')):
		if slot == 'b' or slot == 'B':# option to go back to previous state of flowchart
			selectdist(age_group,dose,state_name,client_conn)
		elif slot == 'q' or slot == 'Q':#option for user to quit the program voluntarily
			print("Client wants to quit!")
			print("Saying Bye to client and closing the connection!")
			stopCommunication(client_conn)
		else:
			dic = fetchVaccineSlots(web_page_data, hos, dist_name, state_name, age_group, dose).get(slot)
			day = list(dic.keys())[0]
			num = dic.get(day)
			print("Vaccination Date selected:  %s" %day)
			print("Available Slots on that date:  %s" %num)
			m2 = "\n<<< Selected Vaccination Appointment Date: "+str(day)
			m2 = m2+"\n<<< Available Slots on the selected Date: "+str(num)
			if int(num) > 0:
				m2 = m2+"\n<<< Your appointment is scheduled. Make sure to carry ID Proof while you visit Vaccination Center!'"
				client_conn.send(m2.encode())
				stopCommunication(client_conn)
			elif int(num) == 0:
				m2 = m2+"\n<<< Selected Appointment Date has no available slots, select another date!"
				client_conn.send(m2.encode())
				selectslot(age_group,dose,state_name,dist_name,hos,client_conn)
	else:
		if invalid == 3:
			stopCommunication(client_conn)
		else:
			invalid = invalid + 1
			m2 = "<<< Invalid input provided " + str(invalid) + " time(s)! Try again.\n"
			client_conn.send(m2.encode())
			if invalid == 3:
				stopCommunication(client_conn)
			else:
				selectslot(age_group,dose,state_name,dist_name,hos,client_conn)
##############################################################


if __name__ == '__main__':
	"""Main function, code begins here
	"""
	url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	web_page_data = fetchWebsiteData(url_website)
	client_conn, client_addr = openConnection()
	startCommunication(client_conn, client_addr, web_page_data)
