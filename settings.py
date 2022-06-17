class Settings:
    TOKEN = "Bearer keyWmw6EK3iTDxyjs"
    AUTH_TOKEN_HEADER = {
        "Authorization": TOKEN, 
        "Content-Type": 'application/json'
        }
    
    TABLE_NAME = 'Cars'
    BASE_ID = 'appsHG9hnixeQKWCY' 

    LIST_RECORDS_URL  = '?maxRecords=3&view=Grid%20view' 
   


    @property
    def get_url(self):
       return f'https://api.airtable.com/v0/{self.BASE_ID}/{self.TABLE_NAME}'
    


settings = Settings()