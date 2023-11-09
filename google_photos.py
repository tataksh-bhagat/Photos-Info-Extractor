from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

# The scope for the OAuth2 request.
SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']

def list_albums(service):
    try:
        results = service.albums().list(pageSize=50, excludeNonAppCreatedData=False).execute()
        albums = results.get('albums', [])
        for album in albums:
            print(f"Album title: {album['title']}, Album ID: {album['id']}")
    except Exception as e:
        print(e)


def login_to_google_photos():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=64374)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Manually specify the discovery document URL
    discovery_service_url = 'https://photoslibrary.googleapis.com/$discovery/rest?version=v1'

    # Build the service object using the discovery document
    service = build('photoslibrary', 'v1', credentials=creds, discoveryServiceUrl=discovery_service_url)
    return service

def list_album_photos(service, album_id):
    try:
        nextPageToken = None
        while True:
            request_body = {
                'albumId': album_id,
                'pageSize': 100,  # Adjust pageSize if needed (maximum is 100)
                'pageToken': nextPageToken
            }
            results = service.mediaItems().search(body=request_body).execute()
            items = results.get('mediaItems', [])
            for item in items:
                print(item['filename'])  # Print only the filename

            nextPageToken = results.get('nextPageToken')
            if not nextPageToken:
                break
    except Exception as e:
        print(f"An error occurred: {e}")




if __name__ == '__main__':
    service = login_to_google_photos()
    print()
    print("All the albums in your Google Photos Account are: ")
    print()
    list_albums(service) 

    print()
    album_id = input("Please copy the Album ID from above and paste here: ")

    service = login_to_google_photos()
    # You need to replace 'YOUR_ALBUM_ID' with the actual album ID.
    list_album_photos(service, album_id)


