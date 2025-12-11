import requests
import sys
import argparse
import os

def send_request(project_id, key):
    url = f"https://firebaseremoteconfig.googleapis.com:443/v1/projects/{project_id}/namespaces/firebase:fetch"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36", "X-Goog-Api-Key": key, "Content-Type": "application/json"}
    json={"appId": f"0:{project_id}:web:41a52066080fc6b83f909f", "appInstanceId": "XD"}
    res = requests.post(url, headers=headers, json=json)
    return res.json()

def print_readable(data, indent=0):
    for key, value in data.items():
        prefix = '  ' * indent + f"- {key}: "
        if isinstance(value, dict):
            print(f"{prefix}")
            print_readable(value, indent + 1)
        elif isinstance(value, list):
            print(f"{prefix}[")
            for item in value:
                if isinstance(item, dict):
                    print_readable(item, indent + 2)
                else:
                    print("  " * (indent + 2) + f"- {item}")
            print("  " * indent + "]")
        else:
            print(f"{prefix}{value}")
    
def main():
    parser = argparse.ArgumentParser(description="Fetch Firebase Remote Config data.", add_help=True)
    parser.add_argument("-p","--project_id", type=str, help="Firebase project ID or term to search, Ex: 92362652315 or weluproject", required=True)
    parser.add_argument("-k","--key", type=str, help="API key for Firebase Remote Config", default=os.environ.get("GOOGLE_API_KEY"))
    args = parser.parse_args()
    project_id = args.project_id
    key = args.key
    
    if project_id.isdigit():
        data = send_request(project_id, key)
        print("="*40)
        print_readable(data)
    else:
        print("Trying to find project ID...")
        response = send_request(project_id, key)
        message = response.get("error", {}).get("message", "Unknown project ID")
        try:
            project_id = message.split("projects/")[1].split("'")[0]
            print(f"Found project ID: {project_id}")
            data = send_request(project_id, key)
            print("="*40)
            print_readable(data)
        except IndexError:
            print("Could not find project ID.")
            sys.exit(1)
        
if __name__ == '__main__':
    main()
