import logging


class ErrorLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname == 'ERROR'
    

class CriticalLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname == 'CRITICAL'
    

class DebugWarningLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname in ('DEBUG','WARNING')