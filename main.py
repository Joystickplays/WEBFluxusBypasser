# type: ignore
from gevent import monkey
monkey.patch_all()
from flask import Flask, request, render_template
import requests
import time
import re
from bs4 import BeautifulSoup as bs
from flask_cors import CORS
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
	return "You can access the client at <a href='https://fluxbypass.upstand.app'>fluxbypass.upstand.app</a>"

@app.route('/bypass')
def bypass():
		hwid = request.args.get('hwid')
		extractedHWID = hwid
		if extractedHWID:
		    headers = {
		        'Referer': 'https://linkvertise.com/',
		        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
		    }
		    print("Initializing")
		    bypass_url = 'https://fluxteam.net/android/checkpoint/start.php?HWID=' + extractedHWID
		    requests.get(bypass_url, headers={'Referer': 'https://fluxteam.net/'})
		    time.sleep(0x1)
		    print("First check")
		    requests.get('https://fluxteam.net/android/checkpoint/check1.php', headers=headers)
		    time.sleep(0x1)
		    response = requests.get('https://fluxteam.net/android/checkpoint/main.php', headers=headers)
		    
		    print('Getting key...')
		    parser = bs(response.text, 'html.parser')
		    print(parser.find("code").get_text())
		    return parser.find("code").get_text()
		else:
		  return "Bad Request", 400
	
if __name__ == '__main__':
	http_server = WSGIServer(('0.0.0.0', 8080), app)
	http_server.serve_forever()
