import sys
from flask import Flask
from housing.logging import logger
from housing.exception import HousingException



app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    
    try:
        raise Exception("WE are testing custom exception")
    except Exception as e:
        raise HousingException(e,sys) from e
        logging.info(housing.error_message)
        logging.info("we are testing logging module")
    
    
    return "starting machine learning project. this is after making change"

if __name__=='__main__':
    app.run(debug = True)