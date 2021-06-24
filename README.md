# pyscripter-er

A terrible fork of https://github.com/lanmaster53/pyscripter-er

Combined all relevant claases into one Python file. Save pyscripterer.py to a folder where you put all your Python extensions for Burp. Go to `Burp > Extender > Options > Pytho Environment` and provide full path to the folder where your Burp Python extensions live. 

Then head over to Extensions and manually add pyscripter.py as a Python extenion. To do this, click "Add" under Burp Extension. under `Extension Detais > Type` choose Python, and provide the path to pyscripter.py. 

Once loaded, you'll see a script tab. Here you provide your Python scripts. 

lanmaster53 provided a really good example of how to identify and create custom issues using PyScripterer. I modified a few lines in his script to start creating HTTP Basic Auth issues. See httpbasicauth.py for that. If you want to use it, you'll need to simply paste its contents into Script tab and it'll start analyzing anything going through Burp and passive scans. 


