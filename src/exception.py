# import sys
# import logging


# def error_message_detail(error,error_detail:sys):
#     _,_,exc_tb=error_detail.exc_info()#it will provide all the detail related to error like where it is occuring and what type of error is this._,_, is blank bcz it takes three types of varibale.
#     file_name = exc_tb.tb_frame.f_code.co_filename #in which file the error occurs.
#     error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
#      file_name,exc_tb.tb_lineno,str(error))
#     return error_message
    
# class CustomException(Exception):
#     def __init__(self,error_message,error_detail : sys):
#         super().__init__(error_message) #we are inheriting the error class here 
#         self.error_message=error_message_detail(error_message,error_detail=error_detail) #we are passing the error message
#         #and error detail to the error_message_detail function and storing the return value in error_message variable
#         #error_message_detail function will return the error message in string format.
#         def __str__(self):
#             return self.error_message
        

# if __name__=="__main__":

#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by Zero error ")
#         raise CustomException(e,sys) 

import sys
import logging

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by Zero error")
#         try:
#             raise CustomException(e, sys)
#         except CustomException as ce:
#             print(ce)  # This will print the custom error message