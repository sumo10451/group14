## Group 14
### Teamates : 
- Hemanth Kumar Anumolu
- Sumanth Dodda
- Ramya Jampani
- Bhavya Sri Killi

## Text-to-Voice (TTS) :: Client and Server Architecture
### Introduction
This Text-to-Voice (TTS) ai project is designed to enable developers to quickly and easily create high-performance, state-of-the-art Text2Speech models for a wide variety of applications. With the help of our Deep Learning models, Speaker Encoder, and Vocoder models, developers can create high-quality synthetic voices for their applications. We provide detailed training logs on the terminal and Tensorboard, as well as fast and efficient model training so that developers can quickly and easily create the best-sounding synthetic voices possible. We also provide tools to curate Text2Speech datasets, utilities to use and test your models, and a modular code base so that developers can easily implement their own ideas. With our TTS ai project, developers can create the best-sounding synthetic voices for their applications. 


### Project plan:
1. Front-end part of the application interface:
We are planning to create a fornt-end part of the application to capture the text that the user wanted to convert into voice. The user inputs a text in the text placeholder like an input field and clicks on a button to convert it into the voice.

2. Text-to-Voice Conversion part:
The text will be captured and sent to the server to process the text-to-voice using the WebRTC. Using the TTS library which is an advanced text-to-voice speech generation library, we will generate the voice output for the text received.

3. Results: 
The output result is then sent back to the front-end application in mp3 or other audio format. user can then interact and listen to the output audio.

Architecture:
This application will be using the frontend web application as the User interface and flask server.


### Iteration 1:
1. we will go through the library first, understand the input and output format. 
2. Installing the basic configurations and software packages required to work with the library.
3. Figure out the technologies, tools, pipelines, and programming languages that will be needed to build the application.
4. Getting familiarized with the tools, languages, and technologies. 

### Iteration 2:
1. working with the model and testing the model for any issues.
2. check if there can be any changes made to the model to improve its accuracy.
3. Basic setup and installation of software packages for developing the web application. 

### Iteration 3:
1. Develop the web application and integrate the text-to-voice model with the application.
2. Testing the application for any red flags or breaks and fix any issues if found.
3. Understanding different inbuilt flags present and understanding and using them better

### Iteration 4:
1. create a deployment pipeline and deploy the project.
2. Testing the project end-to-end and fix any issues if found.
3. Creating a basic HTML page and posting input to the server backend and display output given
4. Deploying it on one of the cloud-based providers to run over the network

### Iteration 5:
1. Self Signed certificates configuration
2. Documentation and presentation for the project delivery.

## Installation
- sudo apt update -y && sudo apt full-upgrade -y
- wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz
- tar zxvf Python-3.10.0.tgz  
- cd Python-3.10.0/
- ./configure --enable-optimizations
- git clone https://github.com/sumo10451/group14.git
- cd group14/
- python3.10 -m pip install -r requirements.txt
- python3.10- -m pip install streamlit
- streamlit run streamlit_audio_converter.py --server-port 80

