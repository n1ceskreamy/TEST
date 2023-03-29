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

_Start_ command will load app, preset values, load settings from sources.

_Key in_ uses instead of hardware signal, there're two keys: "S" and "T" for secure- and technical specialists. 

The update process will start after both keys are activated and it will stop after both keys are activated.

_Stop_ command will terminate all subrocesses in app and clear variables, so we recommend to use it after each logically unique using of app.
