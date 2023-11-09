# Photos-Info-Extractor
A tool to extract information of your images in Google Photos


## How to use the Python script to list the photos in a Google Photos album

**Prerequisites:**

* A Google Cloud Platform account.
* Python 3.7 or higher.
* A virtual environment.

**Steps:**

1. Create a new virtual environment:

python3 -m venv myenv


2. Activate the virtual environment:

source myenv/bin/activate


3. Install the required packages:

pip3 install google-auth-oauthlib
pip3 install google-api-python-client


4. Enable the Google Photos API in the Google Cloud Platform Console:

Go to the Google Cloud Platform Console.
Click the hamburger menu (three horizontal lines) in the top left corner of the page.
Select APIs & Services > Library.
Search for the Google Photos API and click on it.
Click the Enable button.

5. Create an OAuth client ID and download the OAuth 2.0 client credentials file:

In the Google Cloud Platform Console, click the hamburger menu (three horizontal lines) in the top left corner of the page.
Select APIs & Services > Credentials.
Click the Create Credentials button.
Select OAuth client ID from the dropdown menu.
Click the Create button.
Select Application type and click Next.
Select Web application and click Create.
Copy the Client ID and Client secret values.
Click the Download JSON button to download the OAuth 2.0 client credentials file.

6. Place the OAuth 2.0 client credentials file in the same directory as your Python script.

7. Run the Python script:

python3 google_photos.py

Follow the instructions on the screen to authenticate with the Google Photos API.

Enter the album ID of the album that you want to list the photos for.

The script will list all of the photos in the album to the console.

Notes:

If you see a message like // photo attached, you need to put the redirect URL in the Authorized redirect URIs option in Google Cloud.
To add yourself to the test user account for testing, add your email ID to the test users list in Google Cloud.
Example usage:

python3 google_photos.py

Album title: My Vacation Photos, Album ID: 1234567890

Enter the album ID: 1234567890

[1.jpg, 2.jpg, 3.jpg, ...]

You can copy and paste this text into a new file and save it with the .md extension. Once you have saved the file, you can open it in a text editor or a Markdown viewer to see the formatted instructions.
