import logging 
logger = logging.getLogger(__name__)
logging.basicConfig(filename='logfile.log', encoding='utf-8', level = logging.DEBUG)
logging.debug("This should be in log file")
logging.info("this two")
logging.warning("this three")
logging.error("anything can go in the file")
