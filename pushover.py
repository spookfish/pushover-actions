import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="Pushover Notifications")
    parser.add_argument('--token', 
                        type=str, 
                        required=True, 
                        help='Application API token')
    parser.add_argument('--user',
                        type=str, 
                        required=True, 
                        help='User/group key')
    parser.add_argument('--message',
                        type=str, 
                        required=True, 
                        help='Message text')
    parser.add_argument('--title',
                        type=str, 
                        help='Message title')
    parser.add_argument('--url',
                        type=str, 
                        help='Supplementary URL to show with your message')
    parser.add_argument('--url_title',
                        type=str, 
                        help='title for your supplementary URL, otherwise just the URL is shown')
    parser.add_argument('--device',
                        type=str, 
                        help='Device name to send the message directly to')
    args = parser.parse_args()
    try:
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {
            'token'     : args.token,
            'user'      : args.user,
            'message'   : args.message,
            'title'     : args.title,
            'url'       : args.url,
            'url_title' : args.url_title,
            'device'    : args.device,
        }
        response = requests.post('https://api.pushover.net/1/messages.json',
                                 headers=headers,
                                 data=payload,
                                 timeout=60)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        raise e

if __name__ == '__main__':
    main()
