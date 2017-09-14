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
    
    
# Resource Archetype
### Document
    a singular concept

### Collection
    a direcoty of resource
    
### Store
    let client put resource in
    
### Controller
    a REST API relies on controller
    resources to perform application-specific actions that cannot be logically mapped to
    one of the standard methods (create, retrieve, update, and delete, also known as
    CRUD).
    
    Controller names typically appear as the last segment in a URI path, with no child
    resources to follow them in the hierarchy.
    
  * Rule: A plural noun should be used for store names
  * Rule: A verb or verb phrase should be used for controller names
  * Rule: Variable path segments may be substituted with identity-based
values
  * Rule: CRUD function names should not be used in URIs

# Reqeust Method
  * Rule: Always make proper use of HTTP methods
  * Rule: GET must be used to retrieve a representation of a resource
  * Rule: HEAD should be used to retrieve response headers
  
  **difference between PUT and POST**
  * Rule: PUT must be used to both insert and update a stored resource
  * Rule: PUT must be used to update mutable resources
  * Rule: POST must be used to create a new resource in a collection
  * Rule: POST must be used to execute controllers

# Response status code
    Category Description
    1xx: Informational Communicates transfer protocol-level information.
    2xx: Success Indicates that the client’s request was accepted successfully.
    3xx: Redirection Indicates that the client must take some additional action in order to complete their request.
    4xx: Client Error This category of error status codes points the finger at clients.
    5xx: Server Error The server takes responsibility for these error status codes.

  * Rule: 202 (“Accepted”) must be used to indicate successful start of an
asynchronous action
  * Rule: 304 (“Not Modified”) should be used to preserve bandwidth
  * Rule: 400 (“Bad Request”) may be used to indicate nonspecific failure
  * Rule: 401 (“Unauthorized”) must be used when there is a problem with the
client’s credentials
  * Rule: 403 (“Forbidden”) should be used to forbid access regardless of
authorization state
