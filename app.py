from flask import Flask, render_template
import sqlite3
import pathlib 

base_path = pathlib.Path(r'C:\Users\alan\Documents\project\Project_group_8\database')
db_name = "GlobalTerrorism.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    data = cursor.execute("SELECT * FROM data_terrorism limit 10").fetchall()
    con.close()

    return render_template("data_table.html", data=data)

if __name__=="__main__":
    app.run(debug=True)
