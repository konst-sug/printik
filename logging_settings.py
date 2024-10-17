import sys

from log_filters import DebugWarningLogFilter, CriticalLogFilter, ErrorLogFilter


logging_config = {
    'version' : 1,
    'disable_existimg_loggers' : True,
    'formatters' : {
        'default' : {
            'format' : '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_1' : {
            'format' : '[%(asctime)s] #%(levelname)-8s %(filename)s:'
            '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_2' : {
            'format' : '[%(asctime)s] # %(filename)s:'
            '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        }
    },
    'filters' : {
        'critical_filter' : {
            '()' : CriticalLogFilter
        },
        'error_filter' : {
            '()' : ErrorLogFilter
        },
        'debug_warning_filter' : {
            '()' : DebugWarningLogFilter
        }
    },
    'handlers' : {
        'default' : {
            'class' : 'logging.StreamHandler',
            'formatter' : 'default'
        },
        'stdout' :{
            'class' : 'logging.StreamHandler',
            'formatter' : 'formatter_1',
            'filters' : ['error_filter', 'critical_filter'],
            'stream' : sys.stdout
        },
        'debug_file' : {
            'class' : 'logging.FileHandler',
            'filename' : 'debug.logg',
            'mode' : 'w',
            'level' : 'DEBUG',
            'formatter' : 'formatter_2',
            'filters' : ['debug_warning_filter']
        }
    },
    'loggers' : {
        'everlasting_thread' : {
            'level' : 'DEBUG',
            'handlers' : ['debug_file', 'stdout']
        }

    },
    'root' : {
        'formatter' : 'default',
        'handlers' : ['default']
    }
}