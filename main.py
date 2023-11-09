# Import the necessary libraries.
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

# Define the scope for the OAuth2 request.
SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']

# Define a function to list the albums in the user's Google Photos account.
def list_albums(service):
  """Lists the albums in the user's Google Photos account.

  Args:
    service: A Google Photos API service object.
  """

  try:
    # Get a list of the user's albums.
    results = service.albums().list(pageSize=50, excludeNonAppCreatedData=False).execute()
    albums = results.get('albums', [])

    # Print the titles and IDs of the albums.
    for album in albums:
      print(f"Album title: {album['title']}, Album ID: {album['id']}")
  except Exception as e:
    print(e)

# Define a function to log in to Google Photos.
def login_to_google_photos():
  """Logs in to Google Photos and returns a service object.

  Returns:
    A Google Photos API service object.
  """

  creds = None

  # Check if there is a valid token file already.
  if os.path.exists('token.json'):
    # If there is, load the credentials from the token file.
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    # If there are no credentials, create a new OAuth2 flow object.
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)

    # Run the OAuth2 flow and get the user's credentials.
    creds = flow.run_local_server(port=64374)

    # Save the credentials for the next run.
    with open('token.json', 'w') as token:
      token.write(creds.to_json())

  # Manually specify the discovery document URL.
  discovery_service_url = 'https://photoslibrary.googleapis.com/$discovery/rest?version=v1'

  # Build the service object using the discovery document.
  service = build('photoslibrary', 'v1', credentials=creds, discoveryServiceUrl=discovery_service_url)

  return service

# Define a function to list the photos in an album.
def list_album_photos(service, album_id):
  """Lists the photos in an album.

  Args:
    service: A Google Photos API service object.
    album_id: The ID of the album to list the photos in.
  """

  nextPageToken = None
  while True:
    # Get the next page of photos in the album.
    request_body = {
        'albumId': album_id,
        'pageSize': 100,  # Adjust pageSize if needed (maximum is 100)
        'pageToken': nextPageToken
    }
    results = service.mediaItems().search(body=request_body).execute()
    items = results.get('mediaItems', [])

    # Print the filenames of the photos.
    for item in items:
      print(item['filename'])

    # Get the next page token.
    nextPageToken = results.get('nextPageToken')

    # If there is no next page token, break out of the loop.
    if not nextPageToken:
      break

# The main function.
if __name__ == '__main__':
  # Log in to Google Photos.
  service = login_to_google_photos()

  # List the albums in the user's Google Photos account.
  print()
  print("All the albums in your Google Photos Account are: ")
  print()
  list_albums(service)

  # Ask the user for the ID of the album to list the photos in.
  print()
  album_id = input("Please copy the Album ID from above and paste here: ")

  # List the photos in the album.
  service = login_to_google_photos()
  print()
  print("All the images in your Google Photos Album are: ")
  print()
  list_album_photos(service, album_id)
  print()
  print("End of Program")
  print()
