from flask import Flask, url_for, request, redirect
import os
import requests
#import sys
access_token='EAAE8Mxa59ZBsBAO5j21u4oPrQNHNQfFG9hLbpZCVwpzrrHlZA8NK3UY9ZBFjC3QbhLrVkswklQdrlsLTrj9I2YDwr0smZBkxITw1DzTFXZBnWHxoXYjZCbfNsMa0CPeNQmBO0JgD2Pj7BwrAZAQcW3ZBc7gAQxHrK3r3crMFFOencNwZDZD'
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_file=os.path.join(APP_ROOT, '/home/praks/FlaskApp/')

@app.route('/')
def me():
    return "Testing bot"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        user=request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/success/<name>')
def success(name):
    return 'Hello there! %s' %name

@app.route('/webhook/', methods=['GET','POST'])
def webhook():
    if(request.method=='GET'):
        if request.args.get('hub.verify_token') == 'secret':
            return request.args.get('hub.challenge')
        else:
            return 'Error, wrong validation token'

    else:
        #f_openfile=open(os.path.join(APP_file,'request.json'),'r+')
        #f_openfile.write("success \n")
        
        
        data = request.json
        print(data)


        #f_openfile.write(data)
        #f_openfile.close()
        messaging_events = data['entry'][0]['messaging']

        for event in messaging_events:
            sender = event['sender']['id']

        payload = {
                    "recipient": { "id": sender},
                    "message": {"text":"Hi there!"} }
        r=requests.post('https://graph.facebook.com/v2.6/me/messages', params={'access_token': access_token}, json=payload)
        return "ok"

        #write post method

#347665098995691 app id
#access token
#EAAE8Mxa59ZBsBAO5j21u4oPrQNHNQfFG9hLbpZCVwpzrrHlZA8NK3UY9ZBFjC3QbhLrVkswklQdrlsLTrj9I2YDwr0smZBkxITw1DzTFXZBnWHxoXYjZCbfNsMa0CPeNQmBO0JgD2Pj7BwrAZAQcW3ZBc7gAQxHrK3r3crMFFOencNwZDZD


#Normal way of doing. Omitted for pythonanywhere.
if __name__=='__main__':
    app.run(debug=True)

