# Importe
import shutil
from Logging.logging_beispiel import logs
from time import sleep

if __name__ == '__main__':

    path = '/'

    BytesPerGB = 1024 * 1024 * 1024

    logger = logs(logfile='speicherplatz.log', loglevel='WARNING')

    while True:
        (total, used, free) = shutil.disk_usage(path)
        free_disc_usage = float(free/BytesPerGB)
        if free_disc_usage < 50:
            logger.critical(f"Freier Speicher: %.2fGB" % (free_disc_usage))
        elif 50 < free_disc_usage < 100:
            logger.warning(f"Freier Speicher: %.2fGB" % (free_disc_usage))
        else:
            logger.info(f"Freier Speicher: %.2fGB" % (free_disc_usage))
        sleep(60)