from urllib.request import urlopen

try:
    response = urlopen("http://example.com")
    html = response.read()
    print("Got it")
except IOError as e:
    print(f"An error occured {e}")