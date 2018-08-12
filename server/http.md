# General HTTP
    PUT vs POST
    PUT Store data from client into a named server resource.
    POST Send client data into a server gateway application.
    
    Telnet can act as a HTTP client
    nc is more powerful
    
# Security
    Fat URL: generate special URL for each user. Add extra info in the URL
    Cookies: session cookie, persistent cookie
              Response with header "Set-Cookie: ..."
              Request with header "Cookie: ..."
                The browser remembers the cookie contents sent back from the server in Set-Cookie or Set-Cookie2
                headers, storing the set of cookies in a browser cookie database (think of it like a suitcase with stickers
                from various countries on it). When the user returns to the same site in the future , the browser will select those                       cookies slapped onto the user by that server and pass them back in a Cookie request header.
