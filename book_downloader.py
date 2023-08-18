import os
import json
import base64
import sys
import argparse

def download_preview(base64_data, save_path):
    image_data = base64.b64decode(base64_data)
    with open(save_path, 'wb') as f:
        f.write(image_data)


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
    args = parser.parse_args()

    if args.file_path is None:
        print('Enter valid .har file path')
        parser.print_help()
        exit()

    if args.search_url is None:
        print('Enter valid search url to find in the .har file')
        parser.print_help()
        exit()

    if args.mime is None:
        print('Enter valid search mimeType to find in the .har file. e.x image/png, image/jpeg')
        parser.print_help()
        exit()

    if not os.path.exists(args.file_path):
        print('.Har File does not exist at {}'.format(args.file_path))
        parser.print_help()
        exit()

    with open(args.file_path, 'rb') as f:  # Open in binary mode
        data = f.read()
    har = json.loads(data.decode('utf-8'))

    os.makedirs(args.export_path, exist_ok=True)

    i = 0
    ext = args.ext.lower()
    for entry in har['log']['entries']:
        if args.search_url in entry['request']['url']:
            if args.mime in entry['response']['content']['mimeType']:
                base64_data = entry['response']['content']['text']
                image_name = '{}_Image.{}'.format(i, ext)
                save_path = os.path.join(args.export_path, image_name)
                download_preview(base64_data, save_path)
                print(f'Exported file: {image_name}')
                i += 1
    if i == 0:
        print("""
            Seems like no file has been exported.
            Please check the response > content > mimeType in .har file
        """)
    print('Export process completed.')

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        print(e)
        sys.exit(1)
