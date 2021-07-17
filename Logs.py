import logging


logging.basicConfig(filename="E://Software//Pyhton-Sel//logs//test.log" ,
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S:%p')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug message")
logger.info("This is info msg")
logger.error("This is error msg")
logger.warning("This is warning msg")
logger.critical("This is critical msg")
