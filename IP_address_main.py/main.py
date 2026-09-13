import socket

while True:
    website = input("\nEnter website (e.g. google.com, or 'exit' to quit): ").strip()

    if website.lower() == "exit":
        break

    # Strip out http://, https://, or trailing slashes if accidentally entered
    website = website.replace("https://", "").replace("http://", "").split("/")[0]

    try:
        ip = socket.gethostbyname(website)
        print(f"IP address of {website}: {ip}")
    except socket.gaierror:
        print(f"Could not resolve hostname: '{website}'. Please check the spelling.")