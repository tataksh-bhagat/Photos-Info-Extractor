
# Google Photos Album Photo List Script

## Need of this Project
This project was conceived out of a personal necessity to manage and access a dual-copy photo library more efficiently. As a Google Pixel phone user, I benefit from the unlimited backup feature for photos, which ensures that my pictures are available on any device. However, despite the convenience of cloud storage, I am committed to maintaining original quality backups of my photos and videos on an external hard drive.

The challenge arises when attempting to retrieve specific high-quality images from the hard drive, where they are stored en masse in a single folder. Here, Google Photos' robust indexing system becomes invaluable. By creating albums in Google Photos based on specific criteria—be it faces, pets, or places—I am able to organize the images conveniently.

The purpose of this tool is to streamline the process of aligning my hard drive's content with my Google Photos albums. It fetches the filenames of photos from a specified Google Photos album, making it effortless to identify and transfer these files from the external hard drive to my laptop, ensuring that I always have ready access to the original, high-quality versions of my images, irrespective of my location or the device in use.

By bridging the gap between cloud and physical storage, this tool enhances my workflow, provides a safeguard for my digital memories, and delivers peace of mind that comes from having a reliable and personal archival system.

## Instructions for New Users

### Prerequisites
- A Google Cloud Platform account.
- Python 3.7 or higher installed on your system.

### Set Up Python Virtual Environment

#### Create a New Environment
Create a new virtual environment by running the following command in your terminal:

```bash
python -m venv myenv
```

#### Activate the Environment
Activate the virtual environment with:

On Unix or MacOS:

```bash
source myenv/bin/activate
```

On Windows:

```cmd
myenv\Scripts\activate
```

#### Install Required Packages
Install the required packages using `pip`:

```bash
pip install google-auth-oauthlib
pip install google-api-python-client
```

### Create a New Project
1. Go to the [Google Cloud Platform Console](https://console.cloud.google.com/).
2. Click the hamburger menu (three horizontal lines) in the top left corner.
3. Select `Projects`.
4. Click the `Create Project` button.
5. Enter a name for your project and select `Create`.

### Enable the Google Photos API
1. In the Google Cloud Platform Console, click the hamburger menu.
2. Navigate to `APIs & Services` > `Library`.
3. Search for "Google Photos API" and select it.
4. Click `Enable`.

### Create an OAuth Client ID
1. In the Google Cloud Platform Console, access the hamburger menu.
2. Go to `APIs & Services` > `Credentials`.
3. Select `Create Credentials` and choose `OAuth client ID`.
4. Click `Create`.
5. Select `Application type` and proceed to `Next`.
6. Choose `Web application` and select `Create`.
7. Download the JSON file for the OAuth client ID.

### Place the OAuth 2.0 Client Credentials File
Move the downloaded OAuth 2.0 client credentials JSON file to the same directory as your Python script.
Make sure the file is named `credentials.json`

### Authenticate with the Google Photos API
1. Execute the Python script with the command: `python3 google_photos.py`
2. Follow the on-screen instructions to authenticate with the Google Photos API.

### List the Photos in a Google Photos Album
1. After authentication, input the album ID when prompted.
2. Press `Enter`.
3. The script will output the list of photos in the specified album to the console.

### Sample Output

```bash
All the images in your Google Photos Album are: 

IMG_7968.HEIC
IMG_7967.HEIC
IMG_7966.HEIC
IMG_7965.HEIC
IMG_7964.HEIC
IMG_7963.HEIC
IMG_7962.HEIC

End of Program
```

### Bonus Tip
Use the command below to copy files from one folder to a new destination. 
This command is designed to handle file names that include spaces.

```bash
while IFS= read -r file; do cp "$file" '/path/to/destiantion/folder/'; done < '/path/to/plain-text-file-with-photos-names.txt'
```

