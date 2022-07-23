from flask import Flask, request, render_template, jsonify
import pandas as pd
import pickle

app = Flask(__name__)


@app.route("/")
def loadPage():
	return render_template('home.html')

@app.route("/predict", methods=['POST'])
def predict():
    query1 = float(request.form['query1'])
    query2 = float(request.form['query2'])
    query3 = float(request.form['query3'])
    query4 = float(request.form['query4'])
    query5 = float(request.form['query5'])
    query6 = float(request.form['query6'])
    query7 = float(request.form['query7'])
    query8 = float(request.form['query8'])

    data  = [[query1,query2,query3,query4,query5,query6,query7,query8]]
    new_df = pd.DataFrame(data)
    model = pickle.load(open("redbook_magazine_model.sav", "rb"))
    affair = float(model.predict(new_df))
    if affair == 0:
        affair_out="Yes"
    else:
        affair_out="No"
    
    output="Chances of your affair is: {}".format(affair_out)


    return render_template('home.html', output1=output, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'],query6 = request.form['query6'], query7 = request.form['query7'],query8 = request.form['query8'])
    #return render_template('home.html', output1=price)


@app.route("/via_postman", methods=["post"])
def affairs_status():
    if (request.method=='POST'):
        rate_marriage = float(request.json["rate_marriage"])
        age = float(request.json["age"])
        yrs_married = float(request.json["yrs_married"])
        children = float(request.json["children"])
        religious = float(request.json["religious"])
        educ = float(request.json["educ"])
        occupation = float(request.json["occupation"])
        occupation_husb = float(request.json["occupation_husb"])


        data  = [[rate_marriage,age,yrs_married,children,religious,educ,occupation,occupation_husb]]
        new_df = pd.DataFrame(data)
        model = pickle.load(open("redbook_magazine_model.sav", "rb"))
        affair = model.predict(new_df)
        return(jsonify(int(affair)))


if __name__ == "__main__":
    app.run(debug=True)

