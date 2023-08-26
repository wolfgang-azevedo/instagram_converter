# Instagram JSON to CSV Converter

This project provides a simple GUI tool to convert Instagram "Following" and "Followers" JSON files into a single CSV file.

## Objectives

1. Convert "Following" and "Followers" JSON data from Instagram into a single CSV.
2. The CSV file contains columns for URL, Profile, Following back status, and the type (whether the profile is a follower, following, or both).

## Prerequisites

### Downloading your Instagram Data

Before using the script, you need to obtain your Instagram data in JSON format. Follow the steps below to do so:

1. [Request a download of your Instagram data.](https://www.instagram.com/download/request/)
2. After requesting the data, Instagram will send you an email with a link to download a ZIP file.
3. Download the ZIP file and extract it on your computer.
4. Navigate to the `followers_and_following` folder. The two essential files for this script are:
   - `followers_1.json`
   - `following.json`

### Python Setup

- Python 3.8+
- Tkinter (standard library in Python, no need to install separately)

## Getting Started

1. Clone the repository to your local machine:
```
  git clone https://github.com/wolfgang-azevedo/instagram_converter.git
```
2. Navigate to the project directory:
```
  cd path-to-project-directory
```
3. Run the script:
```
  python insta_converter.py
```
4. Follow the instructions in the GUI to select the JSON files and generate the CSV output.

## Modules Used

- `tkinter` for the GUI.
- `json` to handle JSON files.
- `csv` to generate CSV files.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

