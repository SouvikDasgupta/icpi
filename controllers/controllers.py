from basecontrollers import BaseController 
from constants.constants import Constants
from transformer.transformers import ExceptionTransformers
from repository.dboperations import DBOperations


#Subcription controller
class SubscriptionController(BaseController):

	def __init__(self):
		pass

	def subscribe(self, subscribedUser):
		from utility.utilities import validateEmail, generateUniqueId
		isEmailValidated = validateEmail(subscribedUser.get('email'))
		if(isEmailValidated):
			from models.models import SubscribedUser
			subscriptionData =  SubscribedUser(str(generateUniqueId()), subscribedUser.get('email'), True)
			return DBOperations().susbscribe(subscriptionData)
		else:
			return ExceptionTransformers().transformExceptionSubcribedUser(Constants.INVALID_INPUT, Constants.INVALID_EMAIL, Constants.STATUS_FAILED)


#Admin Controller
class AdminController(BaseController):
	def __init__(self):
		self.dbConnection = DBOperations()

	def getUsers(self, userType):
		userList = []
		if userType == 'subscribers':
			from models.models import SubscribedUser
			modelList = self.dbConnection.getUsers(SubscribedUser)
			for user in modelList:
				userList.append(user.email)
			return userList


	def unsubscribeUser(self, email):
		response = self.dbConnection.unsubscribeUser(email)
		return response

	#insert cook basic details
	def addCookDetails(self, cookBasic):
		from utility.utilities import generateUniqueId, generateCompanyId
		from models.models import CookBasicDetails
		lengthOfTable = self.dbConnection.getLengthOfTable(CookBasicDetails)
		companyId = str(generateCompanyId(lengthOfTable))
		cookBasicDetails = CookBasicDetails(str(generateUniqueId()), companyId, cookBasic.get('name'), cookBasic.get('phone')
			, cookBasic.get('email') , cookBasic.get('joiningDate'), cookBasic.get('nativePlace'), cookBasic.get('currentPlace')
			, cookBasic.get('experience'), cookBasic.get('cookStatus'), cookBasic.get('leavingDate')
			, cookBasic.get('dob'), cookBasic.get('gender'))

		return (self.dbConnection.addCookBasicDetais(cookBasicDetails))




#Career Controller 
class CareerController(BaseController):

	def __init__(self):
		self.dbConnection = DBOperations()

	def insertUserInCareers(self, userCareer):
		from utility.utilities import generateUniqueId
		from models.models import Careers
		phone = userCareer.get('phone')
		email = userCareer.get('email')
		career = Careers(str(generateUniqueId()), userCareer.get('name'), email, phone, userCareer.get('role'))
		return self.dbConnection.insertUserInCareers(career)

#ContactUs Controller 

class ContactUsController(BaseController):

	def __init__(self):
		self.dbConnection = DBOperations()

	def insertContactUsDetails(self, contactUsDetails):
		from utility.utilities import validateEmail, validatePhoneNumber, generateUniqueId
		isEmailValidated = validateEmail(contactUsDetails.get('email'))
		# isPhoneValidated = validatePhoneNumber(contactUsDetails.get('phone'))
		if isEmailValidated:
			from models.models import ContactUs
			contactUsModel = ContactUs(str(generateUniqueId()), contactUsDetails.get('name'), contactUsDetails.get('email'), contactUsDetails.get('phone'))
			return self.dbConnection.insertContactUsDetails(contactUsModel)
		else:
			return ExceptionTransformers().transformExceptionContactUs(Constants.INVALID_INPUT, Constants.INVALID_EMAIL, Constants.STATUS_FAILED)















