import requests 

def fetch_randomUser ():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data"  in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country  =user_data["location"]["country"]
        return username, country
    else: 
        raise Exception("failed to fetch user data ")
        return username

fetch_randomUser()
def main():
    try:
        username, country = fetch_randomUser()
        print(f"Username: {username}, Country: {country}")
    except Exception as e:
        print(f"An error occurred: {e}")  
    pass
if __name__ == "__main__":
    main()  