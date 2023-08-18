The PngExportFrom HAR project enables users to download PDF files that may be blocked by certain PDF
viewer sites, such as ebookcentral.proquest.com.

To use the project, users must input a .har file containing the server response for the individual PDF pages. 

To retrieve and export the stream as a .har file, users should follow the steps provided.
It is important to note that the stream must be analyzed using the developer tools network tab in order to convert it into a PNG file.

Chrome:
    Open the Chrome browser.
    Go to the web page that you want to export a .har file for.
    Click on the three dots in the top right corner of the browser window.
    Select More tools > Developer tools.
    In the developer tools window, click on the Network tab.
    Reproduce the problem that you are having.
    Click on the Export button (it looks like a floppy disk).
    Save the file as a .har file.

Firefox:
    Open the Firefox browser.
    Go to the web page that you want to export a .har file for.
    Press Ctrl+Shift+E to open the developer tools.
    In the developer tools window, click on the Network tab.
    Reproduce the problem that you are having.
    Right-click anywhere in the File column and select Save All As HAR.
    Save the file as a .har file.
