import configparser
from Logging.logging_beispiel import logs

class Initial:
    logpath = ''
    loglevel = ''

    def load(self, filename='config.ini'):
        try:
            config = configparser.ConfigParser()
            try:
                config.read(filename)
            except Exception as e:
                print("Fehler: Konfigurationsdatei konnte nicht geöffnet werden!")
                return None
            self.logpath = config.get('Logging', 'path')
            self.loglevel = config.get('Logging', 'loglevel')
            # config.set('Logging', 'wert', '1000')
            # with open('config2.ini', 'w') as file:
            #     config.write(file)
            config.clear()
            return True
        except Exception as e_konfig:
            print(f'Fehler beim lesen der Konfigurationsdatei: {e_konfig}')
            return None


if __name__ == '__main__':
    init = Initial()
    init.load()
    print(f"Ablagepfad Log: {init.logpath}")
    print(f"Loglevel: {init.loglevel}")
    logger = logs(logfile='beispiel_konfigurationsdatei.log', log_path=init.logpath, loglevel=init.loglevel)
    logger.info('Starte Logging')
    logger.warning('Schreibe eine Warnung')
    logger.error('Schreibe einen Fehler')