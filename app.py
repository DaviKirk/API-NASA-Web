from flask import Flask, render_template
import requests

app=Flask(__name__, template_folder="views")

API_KEY = "YTd8YbV8UzkdTJ4RvgyqxnUJkZHjHdVgpb0WkCNq"
    

@app.route('/')
def Home():
    
    IMG_NUM = 9
    API_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&count={IMG_NUM}"
    
    
    response = requests.get(API_URL)
    imgList = response.json()
    
    return render_template("index.html", imgList=imgList)

@app.route('/infoImage/<date>')
def infoImage(date):
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={date}")
    imgInfo = response.json()
    return render_template('info.html', imgInfo=imgInfo)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)