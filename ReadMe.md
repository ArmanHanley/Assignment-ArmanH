# Project Implementation Instructions


This document explains how to implement the feature flags from LaunchDarkly using the Python SDK.


## Prerequisites - Building the Feature Flag

1. Start a free trial with LaunchDarkly at https://launchdarkly.com/start-trial/

2. Create a feature flag called "launch_region_flag"

3. Set the flag variation to type 'String'

4. Create 5 Variations for this feature flag:

		Variation 1 : ireland.png
		Variation 2 : france.png
		Variation 3 : spain.png
		Variation 4 : portugal.png
		Variation 5 : null.png

5. Set the Default ON to Variation 1

6. Set the Default OFF to Variation 5

7. Save the flag

8. Click on the feature flag you just created and go to the targetting menu. We are going to create 4 targetting rules.

9. Under the 'Target users who match these rules' section, click 'Add Rule'

10. Create a rule where 'IF country contains value Ireland', Serve ireland.png

11. Repeat step 10 three more times for Spain, France and Portugal.

12. You should now have 4 rules in total whereby if the country is X then the rule will serve x.png

13. At the bottom of the targeting page, set the Default Rule to serve null.png and if targeting is off, serve null.png.



### Mac Users


1. Download the full ZIP file 'LaunchDarkly-Assignment-ArmanH' from Github.

2. Unzip the file where you would like to store it.

3. In that folder, delete the folder fl_venv.

4. Edit assignment.py and replace the SDK key in line 18 with the key generated in your own environment and save it.

5. Open Terminal on your Mac and navigate to the folder you unzipped using the 'cd' command. You should be within the 'LaunchDarkly-Assignment-ArmanH' directory now within Terminal

6. Next, we need to setup a virtual environment within this folder. We can do so by running the command 'python3 -m venv fl_venv' and click enter. Next we need to activate it by typing : '. fl_venv/bin/activate'. You should see the name fl_venv before the Command Prompt now which means it is activated.

7. Next we need to install Flask in the virtual environment. To do this type : 'pip install Flask' and hit enter. Flask should be installed successfully in the virtual environment.

8. If step 7 didn't work, you may need to install Pip. To install Pip type 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py' and click enter. After that executes type 'python3 get-pip.py' to run the program. Pip should be installed successfully now. Repeat step 7.

9. Next we need to install the LaunchDarkly SDK. Again within the virtual Environment type : `pip install -r requirements.txt` and hit enter. You have now installed the LaunchDarkly Server SDK.

10. If you type : `pip list` and hit enter, you will see Flask and the SDK installed in the virtual environment now.

11. You can now run the python program by typing : `python assignment.py` and hit enter.

12. Copy and paste the URL `http://127.0.0.1:5000` into a web browser to display the HTML page.

13. In LaunchDarkly, turn the feature flag on, refresh the page and you should see the Irish flag displayed. 

14. Turn the feature flag off, refresh the page and you will see a 'null' image displayed.

15. If you are interested in testing the targeting settings, exit the python program in terminal by pressing CTRL+C to quit.

16. Edit assignment.py again but this time edit line 12 and change country to "Spain" instead of "Ireland" and save.

17. Jump back into the terminal again. You should still be within your virtual environment, if not refer to step 7 to activate it again. Run the python program again by typing : `python assignment.py` and hit enter.

18. Refresh the url page `http://127.0.0.1:5000` and you should see the Spanish flag displayed instead. This is because we are using targetting rules to first identify the user's country and based off this information, we are displaying the relavant image to them. If you are still seeing the null image, your feature flag may be turned off so turn this back on in LaunchDarkly.




### Windows Users


















