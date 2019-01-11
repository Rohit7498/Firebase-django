# Firebase-django
A Python app without Firebase is like a chicken without a hen-house; if you don’t have a place to store your eggs, it’s time to re-think the farm.
This app authenticates users through firebase and also lets users create and check report by firebase database query. Also users are able to upload and save files using firebase storage.

<h1>Requirements</h1>
<ul>
  <li>Python 3.x</li>
  <li>Django 2.1</li>
  <li>pip 3</li>
  <li>Pipenv : to create environment</li>
  <li>Firebase console with a new project</li>
</ul>


## Configure FIREBASE 
<ul>
    <li>Open your Firebase Console and Create new project by Selecting Add Project.</li>
    <li>Navigate to Authentication on Dashboard and set SIGN-IN method Email/Password to enable.For first time add a manual user.</li>
    <li>Now, navigate to Project Overview and select Add Firebase to WebApp now, copy config's for later use in Django.</li>
    <li>Now Let's Get started for integrating Firebase with Python Django .</li>
</ul>

## Installing Required Libraries

<h3>Installing Pip:</h3>
<ul>
    <li>Download the get-pip.py installer script. If you're on Python 3.2, you'll need this version of get-pip.py instead. ...
    <li>Open the Command Prompt and navigate to the get-pip.py file.</li>
    <li>Run the following command: python get-pip.py.</li>
  </ul>
  <h3>Installing Pyrebase:</h3>
  <ul>
  <li>Pyrebase is a Python interface to Firebase’s REST API. In layman’s terms, it allows you to use Python to manipulate your Firebase         database. The documentation for Pyrebase can be found at <a href="https://github.com/thisbejim/Pyrebase">Pyrebase</a></li>
  <li>We will install the Pyrebase and its dependencies using pip : pip3 istall pyrebase</li>
  </ul>
  <h3>Insatll Django==2.1 using pip in vitualenv created by pipenv</h3>
  
  # Let's see how does it work:
  
  ## Firebase Database tree:
  
  ![Imgur](https://i.imgur.com/n1s9DKF.png)
  
  ## Simple Login:
  
  ![Imgur](https://i.imgur.com/Ul8hmsb.png)
  
  ## Simple Signup using Firebase Auth:
  
  ![Imgur](https://i.imgur.com/RSP5Etn.png)
  
  ## Homepage:
  
  ![Imgur](https://i.imgur.com/wp9zJiU.png)
  
  ## Create a report in Firebase:
  
  ![Imgur](https://i.imgur.com/SOlORQN.png)
  
  ## Check report:
  Reports are saved with correct timestamp and date of upload with image upload option:
  
  Reports page:
  
  ![Imgur](https://i.imgur.com/0xwmyzd.png)
  
  Detail reports page:
  
  ![Imgur](https://i.imgur.com/zlrf6Ak.png)
  
  
  
  
  
  
  
  
  
  
  
  
