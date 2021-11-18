import logging
import os
import datetime


class Logger(object):
    def __init__(self, name):
        self.outputToFile = True

        # Change the working directory to our script's location
        currentScriptDirectory = os.path.dirname(os.path.realpath(__file__))
        os.chdir(currentScriptDirectory)

        # Create the logs folder if it doesn't already exist
        logsDirectory = os.curdir
        logsDirectory = os.path.join(logsDirectory, "logs")
        if not os.path.exists(logsDirectory):
            os.mkdir(logsDirectory)

        # Get the log file with the date appended to it and set up basic logging
        formatted_date_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        logFilePath = os.path.join(
            logsDirectory, "{0} - LOGS.txt".format(formatted_date_time)
        )
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        fh = logging.FileHandler(logFilePath)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def setLevel(self, level):
        if level.upper() == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
        elif level.upper() == "INFO":
            self.logger.setLevel(logging.INFO)
        elif level.upper() == "WARN":
            self.logger.setLevel(logging.WARN)
        elif level.upper() == "ERROR":
            self.logger.setLevel(logging.ERROR)
        elif level.upper() == "CRITICAL":
            self.logger.setLevel(logging.CRITICAL)
        else:
            self.warn("Invalid log level specified: {0}".format(level))

    def debug(self, message, exception=None):
        output = self.formatMessage(message, exception)
        if logging.getLevelName("DEBUG") >= self.logger.level:
            if self.outputToFile:
                self.logger.debug(output)

    def info(self, message, exception=None):
        output = self.formatMessage(message, exception)
        if logging.getLevelName("INFO") >= self.logger.level:
            if self.outputToFile:
                self.logger.info(output)

    def warn(self, message, exception=None):
        output = self.formatMessage(message, exception)
        if logging.getLevelName("WARN") >= self.logger.level:
            if self.outputToFile:
                self.logger.warning(output)

    def error(self, message, exception=None):
        output = self.formatMessage(message, exception)
        if logging.getLevelName("ERROR") >= self.logger.level:
            if self.outputToFile:
                self.logger.error(output)

    def critical(self, message, exception=None):
        output = self.formatMessage(message, exception)
        if logging.getLevelName("CRITICAL") >= self.logger.level:
            if self.outputToFile:
                self.logger.critical(output)

    def formatMessage(self, message, exception):
        if exception:
            return "{0}\n{1}".format(message, exception)

        return message
