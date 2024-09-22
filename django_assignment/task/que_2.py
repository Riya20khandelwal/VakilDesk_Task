import re
import pandas as pd

def email_check(email):
    EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(EMAIL_REGEX, email):
        return True
    return False

def cleaned_csv(user_data):
    user_data = pd.read_csv(user_data)

    user_data = user_data.drop_duplicates(subset='user_id')
    # print(user_data)
        
    user_data = user_data[user_data['Email'].apply(email_check)]
    # print(user_data)

    return user_data
