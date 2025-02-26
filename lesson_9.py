import requests


def get_data(name: str):
    url = f"https://api.genderize.io?name={name}"
    response = requests.get(url)


    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def parse_data(data: dict):
    if data:
        name = data.get('name')
        gender = data.get('gender')
        probability = data.get('probability')
        print(f"Name: {name}, Gender: {gender}, Probability: {probability}")
    else:
        print("No data to parse.")


name = input("Input Name: ")
data = get_data(name)
parse_data(data)