import os.path
import time
from datetime import datetime

from config import *
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google_parser import google_parser, update_console_prices, update_pc_prices


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    parsed_urls = []
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Сохраняем обновленные данные авторизации
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        start_time = time.time()
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            log.warn("No data found.")
            return

        for row in values:
            if len(row) != 0 and len(row) > 6:
                parsed_urls.append(row[7])
        prices_for_paste = google_parser(parsed_urls)
        console_prices = [[i[0], datetime.now().strftime("%Y-%m-%d %H:%M:%S")] for i in prices_for_paste]
        pc_prices = [[i[1]] for i in prices_for_paste]
        update_console_prices(console_prices)
        update_pc_prices(pc_prices)
        log.debug(f"{result.get('updatedCells')} cells updated.")
    except HttpError as err:
        raise log.error(f"An error occurred: {err}")


if __name__ == "__main__":
    main()
