import requests


def get_location_from_ip():
    try:
        # Use ipinfo.io or ipapi.co to get location based on IP address
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        # Extract latitude and longitude
        loc = data.get("loc", "0,0").split(",")
        latitude = loc[0]
        longitude = loc[1]

        return latitude, longitude
    except requests.exceptions.RequestException as e:
        return f"Error retrieving location: {e}"


# Example usage

if __name__ == "__main__":
    coords = get_location_from_ip()
    print("Current Coordinates:", coords)
