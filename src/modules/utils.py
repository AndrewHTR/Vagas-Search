from dotenv import load_dotenv
import os
load_dotenv()
def get_token():
    token = os.getenv("token")
    if token == None:
        return os.environ["token"]
    return token

def get_site():
    site = os.getenv("site")
    if site == None:
        return os.environ["site"]
    return site