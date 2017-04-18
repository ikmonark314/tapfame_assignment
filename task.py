import requests
import sqlite3
raw_url = "https://itunes.apple.com/us/app/yelp-nearby-restaurants-shopping-services/id284910350?mt=8"
App_Url = raw_url
raw_url = raw_url.split('id')
raw_url = raw_url[-1]
app_Id = raw_url.split('%s')[0]
url = 'https://itunes.apple.com/lookup%sid='+app_Id

response = requests.get(url)

try:
	if response.status_code == 200:
		json_data = response.json()
		json_data = json_data['results']
		data = json_data[0]
		print data.keys()
		
		App_Name = data['sellerName']
		Date_created = data['releaseDate']
		#Description = data['description']
		Screenshots = data['screenshotUrls']
		Genre = data['primaryGenreName']
		Language = data['languageCodesISO2A']
		Currency = data['currency']
		Advisories = data['advisories']
		print 1
		conn = sqlite3.connect('test.db')
		cursor = conn.cursor()
		cursor.execute('''CREATE TABLE APP_INFORMATION (APP_NAME text, DATE_CREATED text, Description text, Screenshots text, Genre text, Language text, Currency text, Advisories text)''')
		cursor.execute('INSERT INTO APP_INFORMATION VALUES(%s,%s,%s,%s,%s,%s,%s,%s)' % (App_Name,Date_created,Description,Screenshots,Genre,Language,Currency,Advisories))
		conn.commit()
		conn.close()
 		print 2

except Exception as e:
	 print str(e)
	

