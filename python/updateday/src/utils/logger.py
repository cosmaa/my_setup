import logging


class Color:
    """A class for terminal color codes."""

    BOLD = "\033[1m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    PURPLE = "\033[95m"
    BOLD_WHITE = BOLD + WHITE
    BOLD_BLUE = BOLD + BLUE
    BOLD_GREEN = BOLD + GREEN
    BOLD_YELLOW = BOLD + YELLOW
    BOLD_PURPLE= BOLD + PURPLE
    BOLD_RED = BOLD + RED
    END = "\033[0m"


class ColorLogFormatter(logging.Formatter):
    """A class for formatting colored logs."""

    FORMAT = "%(asctime)s - %(prefix)s %(levelname)s \t : \t  (%(filename)s) - %(message)s  %(suffix)s"

    LOG_LEVEL_COLOR = {
        "DEBUG": {'prefix': '', 'suffix': ''},
        "INFO": {'prefix': Color.GREEN, 'suffix': Color.END},
        "WARNING": {'prefix': Color.BOLD_YELLOW, 'suffix': Color.END},
        "ERROR": {'prefix': Color.BOLD_RED, 'suffix': Color.END},
        "CRITICAL": {'prefix': Color.BOLD_PURPLE, 'suffix': Color.END},
    }

    def format(self, record):
        """Format log records with a default prefix and suffix to terminal color codes that corresponds to the log level name."""
        if not hasattr(record, 'prefix'):
            record.prefix = self.LOG_LEVEL_COLOR.get(record.levelname.upper()).get('prefix')

        if not hasattr(record, 'suffix'):
            record.suffix = self.LOG_LEVEL_COLOR.get(record.levelname.upper()).get('suffix')

        formatter = logging.Formatter(self.FORMAT)
        return formatter.format(record)
