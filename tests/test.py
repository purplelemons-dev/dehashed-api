from dehashed import Dehashed
from env import API_KEY

dehashed = Dehashed("me@joshsmith.dev", API_KEY)

dehashed.from_email("mzuckerberg@facebook.com")

print(dehashed.entries)
