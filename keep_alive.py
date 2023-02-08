from flask import Flask, render_template, request, session
from threading import Thread
import requests

app = Flask('')
app.secret_key = "secret"

@app.route('/', methods=['GET', 'POST'])
def main():
  error = ""
  suc = ""
  if request.method == 'POST':
    website = request.form['website']
    
    if not website.startswith("http://") and not website.startswith("https://"):
     website = "http://" + website
    try:
      response = requests.get(website)
    except:
      error = "Invalid link!"
      return render_template("index.html", error=error , suc=suc)
      error = ""
      suc = ""
      
    with open("sites.txt", "r") as f:
      lines = f.readlines()
    if website + '\n' in lines:
      error = "Website already exists as a monitor!"
      
    else:
      with open("sites.txt", "a") as f:
        f.write(website + '\n')
      suc="Successfully Added Website to Monitoring!"
  return render_template("index.html", error=error , suc=suc)
  error = ""
  suc = ""


def run():
  app.run(host="0.0.0.0", port=8080)


def keep_alive():
  server = Thread(target=run)
  server.start()
