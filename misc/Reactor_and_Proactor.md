
# Design pattern: Reactor & Proactor

## Reactor:

multi concurrent input 

synchoronous event demultiplexer

initiation dispatcher

event handler is called synchronously. So it must be a short operation and return quickly, otherwise, it will block other events.


## Proactor:

"The proactor pattern can be considered to be an asynchronous variant of the synchronous reactor pattern."

