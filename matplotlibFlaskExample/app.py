import base64
from io import BytesIO
from flask import Flask, render_template
from matplotlib.figure import Figure
import sqlite3

conn=sqlite3.connect('database.db', check_same_thread=False)
curs=conn.cursor()

app = Flask(__name__)

def getHistData (numSamples):
	curs.execute("SELECT * FROM dhtReadings ORDER BY timestamp DESC LIMIT "+str(numSamples))
	data = curs.fetchall()
	dates = []
	temps = []
	hums = []
	for row in reversed(data):
		dates.append(row[0])
		temps.append(row[1])
		hums.append(row[2])
	return dates, temps, hums

def plotTemp():
    times, temps, hums = getHistData(4)
    # Generate the figure **without using pyplot**.
    print("times :",times)
    ys = temps
    xs = times
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3) 
    ax.tick_params(axis="x", which="both", rotation=30)
    ax.plot(xs, ys)
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    #print(data)
    return data

def plotHum():
    times, temps, hums = getHistData(4)
    # Generate the figure **without using pyplot**.
    ys = hums
    xs = times
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3) 
    ax.tick_params(axis="x", which="both", rotation=30) 
    ax.plot(xs, ys)
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    #print(data)
    return data

@app.route("/")
def home():
    temp = plotTemp() 
    hum = plotHum()
    return render_template('index.html', temp = temp, hum = hum)

if __name__ == "__main__":
    app.run()
