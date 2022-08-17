from flask import Flask, render_template            #import flask web framework
import ldclient																			#import LaunchDarkly SDK
from ldclient.config import Config

app = Flask(__name__)

user = {
  "key": "abcdef",
  "firstName": "Arman",
  "lastName": "Hanley",
  "country": "Ireland",
  "user_segment": "beta_tester"
}


@app.route("/")
def get_flag():
	ldclient.set_config(Config("sdk-12d9db02-3e27-4b0f-8acf-c05168cd5d81"))
	show_flag = ldclient.get().variation("launch_region_flag", user, "null.png")
	if (user["user_segment"]) == "beta_tester":
		ldclient.get().close()
		return render_template("beta_tester_HomePage.html", flag=show_flag)
	else:
		return "This is the live version of the website"



if __name__ == "__main__":
	app.run()

