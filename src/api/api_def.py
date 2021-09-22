from flask_restx import Api 

api = Api(version='1.0', title='Todo Application', 
    description = "Todo application for learning how to build flask applications from scratch", 
    catch_all_404s = True
    )
responses = {
    400: "Bad Request", 
    404: "Todo does not exist",
    500: "Internal Server Error" 
}