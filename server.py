from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def mainroute(n=8):
    return render_template("index.html", x=n)

@app.route("/<int:n>/") #Solo funciona con numeros pares
def unparametro(n):
    return render_template("index.html", x=int(n/2),y=4)

@app.route("/<int:n1>/<int:n2>/")  #Con algunos errores también
def dosparametros(n1,n2):
    return render_template("index.html",x=int(n1/2),y=int(n2/2))

if __name__=="__main__":
    app.run(debug=True)