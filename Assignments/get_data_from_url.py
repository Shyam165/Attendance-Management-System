import requests

def get_data_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:  # here 200 means OK
            return response.text
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching data from {url}: {e}")
        return None

def main():
    url = input("Enter the URL to fetch data from: ")
    data = get_data_from_url(url)
    if data:
        print("Data fetched successfully:")
        print(data)

if __name__ == "__main__":
    main()
