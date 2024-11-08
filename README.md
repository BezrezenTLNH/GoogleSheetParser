# Google Sheet Parser
1) Install Python and Dependencies: Make sure you have Python 3.10 (or newer) installed. If you don't have it, install it from the official Python website (https://www.python.org/downloads/).
2) To install project dependencies run:
	2.1) Go to the application folder with the command:
		cd folder-where-you-unzipped-the-app/google_sheet_parser/google_parser
	2.2) Install pip if it is not already installed: python3 -m pip install --upgrade pip
	2.3) Install all necessary dependencies from the requirements.txt file:
		pip install -r requirements.txt
3) Get the unique identifier of your table using the example: 
	https://docs.google.com/spreadsheets/d/`17FT-1WIx_Ya34WvwpeBE7tfLQLGPUURV9Ef8qgZLyLw`/edit?gid=880248886#gid=880248886
	Here the unique identifier will be the part between /d/ and /edit, that is - `17FT-1WIx_Ya34WvwpeBE7tfLQLGPUURV9Ef8qgZLyLw`
4) Set the ID of your table in the config.py file to the value of the SAMPLE_SPREADSHEET_ID variable on line 21, similar to the existing
5) Run the file with the parser:
	python3 main.py
