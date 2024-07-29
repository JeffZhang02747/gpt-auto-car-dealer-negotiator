import configparser

config = configparser.ConfigParser()

def get_personal_setting():
    config.read('settings.ini')
    zipcode = config['USER_INFO']['Zipcode']
    car_model = config['USER_INFO']['CarModel']
    name = config['USER_INFO']['Name']
    dealer_emails = config['USER_INFO']['DealerEmails'].split(', ')
    return {'zipcode': zipcode, 'car_model': car_model, "name": name, "dealer_emails" : dealer_emails}

def get_api_key():
    config.read('settings.ini')
    ApiKey = config['API']['ApiKey']
    return ApiKey
