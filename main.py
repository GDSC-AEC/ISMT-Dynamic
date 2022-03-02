from fastapi import FastAPI
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/organizing")
async def OCommittee():
    # --------------------------------------------------------------------------------------
    # SHEET SETUP
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('static/key/api.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key("1jGMF0OBt8x20C8eLX9u6Qx8sADyy870kLyxE0HO_U2g").sheet1
    # --------------------------------------------------------------------------------------
    x = sheet.col_values(1)
    return x


@app.get("/steering")
async def SCommittee():
    # --------------------------------------------------------------------------------------
    # SHEET SETUP
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('static/key/api.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key("1jGMF0OBt8x20C8eLX9u6Qx8sADyy870kLyxE0HO_U2g").sheet1
    # --------------------------------------------------------------------------------------
    x = sheet.col_values(2)
    return x


@app.get("/international")
async def ICommittee():
    # --------------------------------------------------------------------------------------
    # SHEET SETUP
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('static/key/api.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key("1jGMF0OBt8x20C8eLX9u6Qx8sADyy870kLyxE0HO_U2g").sheet1
    # --------------------------------------------------------------------------------------
    x = sheet.col_values(3)
    return x

@app.get("/technical")
async def TCommittee():
    # --------------------------------------------------------------------------------------
    # SHEET SETUP
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('static/key/api.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key("1jGMF0OBt8x20C8eLX9u6Qx8sADyy870kLyxE0HO_U2g").sheet1
    # --------------------------------------------------------------------------------------
    x = sheet.col_values(5)
    return x

@app.get("/national")
async def NCommittee():
    # --------------------------------------------------------------------------------------
    # SHEET SETUP
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('static/key/api.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key("1jGMF0OBt8x20C8eLX9u6Qx8sADyy870kLyxE0HO_U2g").sheet1
    # --------------------------------------------------------------------------------------
    x = sheet.col_values(4)
    return x
