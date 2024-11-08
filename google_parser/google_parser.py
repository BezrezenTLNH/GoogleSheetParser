import logging
import time
from config import *

import requests
from google.oauth2 import service_account
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


def google_parser(urls: list[str]) -> list[list[int]]:
    prices_for_paste = []
    retry_count = 5
    for url in urls:
        try:
            log.debug(f'Try to parse: {url}')
            response = requests.get(url)
            response.raise_for_status()
            result = response.json()
            console_price = result['console'][-1][-1]
            pc_price = result['pc'][-1][-1]
            log.debug(f'results: console_price: {console_price}, pc_price: {pc_price}')
            prices_for_paste.append([console_price, pc_price])
        except Exception as ex:
            time.sleep(1)
            retry_count -= 1
            if retry_count == 0:
                raise Exception(ex)
    return prices_for_paste


def update_console_prices(prices_for_paste: list[list[int]], spreadsheet_id=SAMPLE_SPREADSHEET_ID, range_name="C2:C",
                          value_input_option="USER_ENTERED"):
    log.debug('Start update_values')
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
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    try:
        service = build("sheets", "v4", credentials=creds)
        body = {"values": [[i[0]] for i in prices_for_paste]}
        print(body)
        result = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body,
            )
            .execute())
        log.debug(f"{result.get('updatedCells')} cells updated.")

        update_time([[i[1]] for i in prices_for_paste])

        return result
    except HttpError as error:
        log.error(f"An error occurred: {error}")
        return error

def update_time(prices_for_paste: list[list], spreadsheet_id=SAMPLE_SPREADSHEET_ID, range_name="I2:I", value_input_option="USER_ENTERED"):
    log.debug('Start update_values')
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
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    try:
        service = build("sheets", "v4", credentials=creds)
        body = {"values": prices_for_paste}
        result = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body,
            )
            .execute())
        log.debug(f"{result.get('updatedCells')} cells updated.")

        return result
    except HttpError as error:
        log.error(f"An error occurred: {error}")
        return error

def update_pc_prices(prices_for_paste: list[list[int]], spreadsheet_id=SAMPLE_SPREADSHEET_ID, range_name="D2:D",
                          value_input_option="USER_ENTERED"):
    log.debug('Start update_values')
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
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    try:
        service = build("sheets", "v4", credentials=creds)
        body = {"values": prices_for_paste}
        result = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body,
            )
            .execute())
        log.debug(f"{result.get('updatedCells')} cells updated.")
        return result
    except HttpError as error:
        log.error(f"An error occurred: {error}")
        return error
