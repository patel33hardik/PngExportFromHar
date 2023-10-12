# PngExportFrom HAR

The **PngExportFrom HAR** project enables users to download PDF files that may be blocked by certain PDF
viewer sites, such as ebookcentral.proquest.com.

## How to Use

To use the project, users must input a `.har` file containing the server response for the individual PDF pages.

To retrieve and export the stream as a `.har` file, users should follow the steps provided.
It is important to note that the stream must be analyzed using the developer tools network tab in order to convert it into a PNG file.

Warning: This code is provided for educational purposes and intended for learning and personal use only. Please use it responsibly and at your own risk. Misuse of this code may have legal implications. The author and contributors are not responsible for any misuse of this code.

### Chrome:
- Open the Chrome browser.
- Go to the web page that you want to export a `.har` file for.
- Click on the three dots in the top right corner of the browser window.
- Select **More tools > Developer tools**.
- In the developer tools window, click on the **Network** tab.
- Reproduce the problem that you are having.
- Click on the **Export** button (it looks like a floppy disk).
- Save the file as a `.har` file.

### Firefox:
- Open the Firefox browser.
- Go to the web page that you want to export a `.har` file for.
- Press `Ctrl+Shift+E` to open the developer tools.
- In the developer tools window, click on the **Network** tab.
- Reproduce the problem that you are having.
- Right-click anywhere in the **File** column and select **Save All As HAR**.
- Save the file as a `.har` file.

## Usage

Once you export the `.har` file, `book_downloader.py` gets as arguments.

```bash
usage: book_downloader.py [-h] [-f FILE_PATH] [-u SEARCH_URL] [-m MIME] [-e EXPORT_PATH] [-ex EXT]

Script execution with output:
$ py book_downloader.py -f har_data/demo.har -u "docImage.action?encrypted=" -m "image/png" -pdf
Downloaded: 0_Image.png
Downloaded: 1_Image.png
Pdf exported successfully!
Export process completed.