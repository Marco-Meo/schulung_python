import logging_beispiel as logging

if __name__ == '__main__':
    logger = logging.logs(logfile='python2.log')
    logger.info("Logging Info")
    logger.warning("Logging Warnung")
    logger.error("Logging Fehler")