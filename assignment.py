from flask import Flask, render_template            # import flask web framework
import ldclient																			# import LaunchDarkly SDK
from ldclient.config import Config

app = Flask(__name__)																# Create instance of Flask Web Application

user = {                                            # Creating a user profile. In reality this wouldn't be a static object
  "key": "abcdef",
  "firstName": "Arman",
  "lastName": "Hanley",
  "country": "Spain",
  "user_segment": "beta_tester"
}


@app.route("/")
def get_flag():																																						# Defining a function to get a regiona flag and present it on a webpage
	ldclient.set_config(Config("sdk-12d9db02-3e27-4b0f-8acf-c05168cd5d81"))									# Using SDK key from our LaunchDarkly environment
	show_flag = ldclient.get().variation("launch_region_flag", user, "null.png")						# Evaluating our first flag
	if (user["user_segment"]) == "beta_tester":																							# If statment evaluating if user is part of the beta_tester group
		ldclient.get().close()
		return render_template("beta_tester_HomePage.html", flag=show_flag)										# If user is in beta_tester group, use render_tempalte function to render a webpage and pass the 'show_flag' output into the HTML file
	else:
		return "This is the live version of the website"																			# If user is not in the beta_tester group return webpage displaying this line.



if __name__ == "__main__":
	app.run()

