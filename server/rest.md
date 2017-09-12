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
  * Rule: GET must be used to retrieve a representation of a resource
  * Rule: HEAD should be used to retrieve response headers
  * Rule: PUT must be used to both insert and update a stored resource
  * Rule: PUT must be used to update mutable resources
  * Rule: POST must be used to create a new resource in a collection
  * Rule: POST must be used to execute controllers
