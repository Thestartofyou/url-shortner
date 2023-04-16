import pyshorteners

# Initialize the pyshorteners client with the desired API
s = pyshorteners.Shortener(api_key='your_api_key_here')

# Enter the URL you want to shorten
long_url = 'https://www.example.com/this-is-a-long-url-that-i-want-to-shorten'

# Shorten the URL
short_url = s.tinyurl.short(long_url)

# Print the shortened URL
print('Short URL:', short_url)
