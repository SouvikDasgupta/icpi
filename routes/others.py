from flask import Flask, Blueprint, request, jsonify, render_template
from transformer.transformers import ExceptionTransformers
from constants.constants import Constants

others = Blueprint('others', __name__)

@others.route('/subscribe', methods=['POST'])
def subscribe():
	try:
		subscribedUser = request.get_json()
	except Exception as e:
		return jsonify(ExceptionTransformers().transformExceptionSubcribedUser(Constants.INVALID_INPUT, str(e), Constants.STATUS_FAILED))
	else:
		from controllers.controllers import SubscriptionController
		return jsonify(SubscriptionController().subscribe(subscribedUser))


@others.route('/careers', methods=['POST'])
def careers():
	try:
		careerDetails = request.get_json()
	except Exception as e:
		return jsonify(ExceptionTransformers().transformExceptionCareer(Constants.INVALID_INPUT, Constants.INVALID_JSON, Constants.STATUS_FAILED))
	else:
		from controllers.controllers import CareerController
		return jsonify(CareerController().insertUserInCareers(careerDetails))

@others.route('/contactus', methods=['POST'])
def contactUs():
	try:
		contactUsDetails = request.get_json()
	except Exception as e:
		return jsonify(ExceptionTransformers().transformExceptionContactUs(Constants.INVALID_INPUT, Constants.INVALID_JSON, Constants.STATUS_FAILED))
	else:
		from controllers.controllers import ContactUsController
		return jsonify(ContactUsController().insertContactUsDetails(contactUsDetails))




