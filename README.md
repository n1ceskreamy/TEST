# Disclaimer 

This is a demo project and shall not be used in production.
The code is distributed under MIT license (see the LICENSE file).


## Running the demo

There is the main options for running the demo:
- containerized (using docker containers)

There shall be docker-compose locally available.

### Running complete demo in containerized mode

execute in VS Code terminal window either
- _make run_
- or _docker-compose up_

then open the requests.rest file in Visual Studio Code editor. If you have the REST client extension installed, you will see 'Send request' active text above GET or POST requests, you can click on it.

Logical order of requests is next: start -> { key_in -> key_in -> { key_out -> key_out }} -> stop
