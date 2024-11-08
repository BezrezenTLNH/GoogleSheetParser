import logging
import os

logging.getLogger("urllib3").setLevel(logging.ERROR)

# логирование
logging.basicConfig(
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
log = logging.getLogger('google.parser')

log_level = os.getenv('LOGLEVEL', 'DEBUG')
assert log_level in ('CRITICAL', 'FATAL', 'ERROR', 'WARN', 'WARNING', 'INFO',
                     'DEBUG', 'NOTSET')
log.setLevel(log_level)

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1EWK1jlL0dV9Y1sAbFjcGhpBpQeezzCai4KGqitfTiTU"

SAMPLE_RANGE_NAME = "FutBin Prices!A2:K"

log.info(f"Configuration: LOGLEVEL={log_level}, SAMPLE_SPREADSHEET_ID: {SAMPLE_SPREADSHEET_ID}, "
         f"SCOPES: {SCOPES}, SAMPLE_RANGE_NAME: {SAMPLE_RANGE_NAME}")
