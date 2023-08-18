import os
import json
import base64
import sys
import argparse

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image


def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


def download_preview(base64_data, save_path):
    image_data = base64.b64decode(base64_data)
    with open(save_path, 'wb') as f:
        f.write(image_data)


def resize_image(image_path, max_width, max_height):
    img = Image(image_path)
    img_width, img_height = img.imageWidth, img.imageHeight

    aspect_ratio = img_width / img_height

    if img_width > max_width:
        img_width = max_width
        img_height = img_width / aspect_ratio

    if img_height > max_height:
        img_height = max_height
        img_width = img_height * aspect_ratio

    img.drawWidth = img_width
    img.drawHeight = img_height
    return img


def exportPdf(image_filenames):
    try:
        pdf_filename = 'Export.pdf'
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

        elements = []
        max_img_width = doc.width - 5
        max_img_height = doc.height - 5

        for image_filename in image_filenames:
            img = resize_image(image_filename, max_img_width, max_img_height)
            elements.append(img)

        # Build the PDF document
        doc.build(elements)
        print_colored('Pdf exported successfully!', '32')
    except Exception as ex:
        print_colored('Exception raised during export pdf: {}'.format(ex), '31')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_path', type=str, help='Please add the .Har file path')
    parser.add_argument(
        '-u', '--search_url', type=str, help='Add url phrase to search in the .har file'
    )
    parser.add_argument(
        '-m', '--mime', type=str, help='Add content mimeType in the .har file'
    )
    parser.add_argument(
        '-e', '--export_path', type=str, default='exported_image',
        help='Export location of the png files'
    )
    parser.add_argument(
        '-ex', '--ext', type=str, default='PNG',
        help='Exported file extension. should be the based on the mimeType e.x. PNG, JPG'
    )
    parser.add_argument(
        '-pdf', '--export_pdf', action='store_true', help='Exported images in the pdf format'
    )
    args = parser.parse_args()

    if args.file_path is None:
        print_colored('Enter valid .har file path', '31')
        parser.print_help()
        exit()

    if args.search_url is None:
        print_colored('Enter valid search url to find in the .har file', '31')
        parser.print_help()
        exit()

    if args.mime is None:
        print_colored(
            'Enter valid search mimeType to find in the .har file. e.x image/png, image/jpeg', '31'
        )
        parser.print_help()
        exit()

    if not os.path.exists(args.file_path):
        print_colored('.Har File does not exist at {}'.format(args.file_path), '31')
        parser.print_help()
        exit()

    with open(args.file_path, 'rb') as f:  # Open in binary mode
        data = f.read()
    har = json.loads(data.decode('utf-8'))

    os.makedirs(args.export_path, exist_ok=True)

    i = 0
    ext = args.ext.lower()
    image_filenames = []
    for entry in har['log']['entries']:
        if args.search_url in entry['request']['url']:
            if args.mime in entry['response']['content']['mimeType']:
                base64_data = entry['response']['content']['text']
                image_name = '{}_Image.{}'.format(i, ext)
                save_path = os.path.join(args.export_path, image_name)
                download_preview(base64_data, save_path)
                image_filenames.append(save_path)
                print(f'Exported file: {image_name}')
                i += 1
    if i == 0:
        print("""
            Seems like no file has been exported.
            Please check the response > content > mimeType in .har file
        """)

    if args.export_pdf:
        if len(image_filenames) > 0:
            exportPdf(image_filenames)

    print_colored('Export process completed.', '32')

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        print(e)
        sys.exit(1)
