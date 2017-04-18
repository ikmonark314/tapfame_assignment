import requests
import sqlite3
# The request library is t request web applications and sqlite3 to access sqlite.
raw_url = "https://itunes.apple.com/us/app/yelp-nearby-restaurants-shopping-services/id284910350?mt=8"#The application url which is having id of application.
App_Url = raw_url                 #
raw_url = raw_url.split('id')     #
raw_url = raw_url[-1]             #
app_Id = raw_url.split('?')[0]    # Extarcting id from url string by spliting it by "id" keyword then by "?" symbol.
url = 'https://itunes.apple.com/lookup?id='+app_Id # The api url which will provide data in json format.

response = requests.get(url)      #  Requesting the api 

try:
	if response.status_code == 200: # The status code 200 means connection establish 

		json_data = response.json()          # Extracting data from json which is having "results" key which stores all required keys. 
		json_data = json_data['results']
		data = json_data[0]
		#print data.keys()
		
		App_Name = data['sellerName']        #
		Date_created = data['releaseDate']   #
		Description = data['description']    #
		Screenshots = data['screenshotUrls'] #
		Genre = data['primaryGenreName']     #
		Language = data['languageCodesISO2A'] #
		Currency = data['currency']          #
		Advisories = data['advisories']      # All the required attributes stored in the respective named variables using keys.

		for i,j,k in zip(Screenshots,Language,Advisories):
			Screenshots[0] = Screenshots[0]+" , "+i
			Language[0] = Language[0]+","+j
			Advisories[0] = Advisories[0]+", "+k            # Merging the list content into single variable so that it can be stored under BLOB data type of sqlite
		Screenshots = Screenshots[0]
		Language = Language[0]
		Advisories = Advisories[0]

		conn = sqlite3.connect('test.db')
		cursor = conn.cursor()
		                                                                                # Connection established with database where test.db is database name.

		create_sql= '''CREATE TABLE APPLICATION_INFO (APP_NAME text, DATE_CREATED text, Description BLOB, Screenshots BLOB, Genre text, Language BLOB, Currency text, Advisories text)'''
		update_sql = '''INSERT INTO APPLICATION_INFO(APP_NAME, DATE_CREATED, Description,Screenshots,Genre,Language,Currency,Advisories) VALUES(?,?,?,?,?,?,?,?)'''
		
		                                                                               # Query Stored in the variable so that it can be access easily also secured.

		cursor.execute(create_sql)
		cursor.execute(update_sql, (App_Name,Date_created,Description,Screenshots,Genre,Language,Currency,Advisories))
																						# Executing the query in which first table is made then values are filled

		conn.commit()                                   
		conn.close()                                                                     # Connection closed and changes commited
 		print "Table Updated..!!"

except Exception as e:
	 print e                                                                             #Prints the exception if arises in above code..
	

