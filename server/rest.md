# REST
    Representational state transfer(REST) is the description for Web's architectural style
    1. client-server
    2. Uniform interface
    3. Layered-system
    4. Cache
    5. Stateless
    6. Code-on-demand
    
    A Web API conforming to the REST architectural style is a REST API. (Web services)
    
# URI
    REST APIs use URI to address resource
    URI syntax:
    URI = scheme "://" authority "/" path ["?" query] ["#" fragment]
    Rule #1: forward slash '/' should be used in path to indicate the hierachical relationship between resources.
             each separated resource should be addressable as standalone resource
    Rule #2: trailing forward slash should not be used in the URI
    Rule #3: Hyphen (-) should be used to improve readability in URI
    Rule #4: underscore (_) should not be used as it might not be visible if underline is added to the URI to indicate it is a link
    Rule #5: lowercase is preferred in URI as URI is case-sensitive except for scheme and authority portion.
    Rule #6: file extension should not be included in the URI but instead using query parameter and response header to indicate the format
    
## URI authority design
    consistent subdomain name should be used, such as:
    https://api.book.org
    https://developer.book.org
    
    
