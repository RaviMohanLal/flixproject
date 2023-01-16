import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string" #original
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 
    # b'\xa2\xee\xae\x95q}\xea\xb92\xf72\x1a\x07s\xc7\x9f'


    #MONGODB_SETTINGS = { 'db' : 'myflixvid' } 
    
    
    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment'}
