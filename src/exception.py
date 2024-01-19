import sys
import logging
#the fn how the error message should look like
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #All the details where the error is (lyk file name, line no etc)
    file_name = exc_tb.tb_frame.f_code.co_filename #Get the file_name (Get it in custom exception handling doc)
    error_message="error occured in python script name [{0}] line number : [{1}] , error message[{2}]".format(
        file_name, exc_tb.tb_lineno,str(error)
    
    )
    return error_message

#Create own Exception class
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) #inherit init fn overrriden the init method
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message #print the error message
    

