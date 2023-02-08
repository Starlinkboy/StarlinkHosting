import time
from keep_alive import keep_alive
import requests

def main():
 while True:
  time.sleep(10)
  with open("sites.txt", "r") as f:
    lines = f.readlines()

  for line in lines:
     response = requests.get(line.strip())
     if response.status_code == 200:
        print(f"Sent a successful ping to {line.strip()}")
     else:
        print(f"Ping to {line.strip()} failed with status code {response.status_code}.")
     

if __name__ == '__main__':
    keep_alive()
    main()
