# Imports
import os
import logging.handlers # https://docs.python.org/3.8/library/logging.handlers.html?highlight=handlers#module-logging.handlers
import sys

# Bespiel für das Loggen
def logs(logfile="pytohn.log", log_path='./logs', loglevel='DEBUG'):
    """Initialisiert der Konfiguration und logger Parameter"""

    log = os.path.join('./logs', logfile)
    try:
        handler = logging.handlers.TimedRotatingFileHandler(log,
                                                            when="midnight",
                                                            interval=1,
                                                            backupCount=31,
                                                            encoding='ISO-8859-1')
    except FileNotFoundError:
        try:
            os.makedirs(log_path)
        except Exception as e:
            print(f"Fehler beim Erstellen des Log Verzeichnis: {e}")
        handler = logging.handlers.TimedRotatingFileHandler(
            log,
            when="midnight",
            interval=1,
            backupCount=31,
            encoding='ISO-8859-1'
        )
    except Exception as e:
        print(f"Fehler beim Erstellen des Logs: {e}")
    frm = logging.Formatter("{asctime} {levelname:8}: {message}", "%d.%m.%Y %H:%M:%S", style="{")
    handler.setFormatter(frm)
    if loglevel == 'DEBUG':
        loglevel = logging.DEBUG
    elif loglevel == 'ERROR':
        loglevel = logging.ERROR
    elif loglevel == 'NOTSET':
        loglevel = logging.NOTSET
    else:
        loglevel = logging.WARNING
    logger = logging.getLogger('python_logger')
    logger.setLevel(loglevel)
    logger.addHandler(handler)
    return logger


if __name__ == '__main__':
    # Initialisiere Logger
    logger = logs()
    logger.info("Programm gestartet")
    systeminfo = sys.implementation
    logger.info(f"System: {systeminfo}")
    try:
        version = sys.getwindowsversion()
        logger.info(version)
    except Exception as e:
        logger.error("System ist nicht Windows basiert")
        logger.error(e)
    logger.warning("Dies ist eine Warnung")
