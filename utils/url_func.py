#functions for url stuff

import re

def url_is_good(url):
    if re.match(r"^(https?://)?(?:www\.)?youtube\.com[/?&#].*$", url, flags=re.IGNORECASE):
        return True
    else:
        return False