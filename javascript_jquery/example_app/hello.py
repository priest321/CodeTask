from flask import render_template, Flask
from markupsafe import escape


app = Flask(__name__)
app.config["SECRET_KEY"] = "A" 


def security(func):
    def warper(*args, **kargs):
        try:
            app.logger.debug(f"security: {kargs}")
            if kargs:
                for k, v in kargs.items():
                    kargs[escape(k)] = escape(v)
            if args:
                args = (escape(key) for key in args)
                
            return func(*args, **kargs)
            
        except Exception as e:
            app.logger.error(f"security warper error: {e}")
        
    return warper



@app.route("/hello/")
@app.route("/hello/<name>")
@security
def hello(name):
    return render_template("hello.html", person=name)
	

if __name__ == "__main__":
    app.run(debug=True)