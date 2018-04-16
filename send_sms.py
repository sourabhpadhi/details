# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, Response, Flask, flash, redirect, render_template, request, session, abort
import plivo
app = Flask(__name__, static_url_path='')


@app.route('/send_sms/')# methods=['POST'])
def outbound_sms():

	client = plivo.RestClient(auth_id = '', auth_token = '')

	try:
		response = client.messages.create(
			src = '1111111111', # Sender's phone number with country code
	    	dst = '917978646880', # Receiver's phone Number with country code
	    	text = 'hello!!!!you have a missed call!!!',
		)
	#response = p.send_message(params)
	# Prints the complete response
		return str(response)
	except plivo.exceptions.PlivoRestError as e:
		print(e)


if __name__ == "__main__":
    app.run(debug=True)
