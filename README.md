# Chatroom Challenge

![Chatroom main window](https://github.com/pauloesteban/chatroom-jobsity/blob/master/files/mainwindow.png)

This project is implemented using Python 3.4.x. For Mac users consider installing [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).

## Requirements
Flask and SocketIO are required. You can install via
```
pip install flask
pip install flask-socketio
```
or in the home folder
```
pip install -r requirements.txt
```

## Usage
Execute on terminal:
```
python main.py
```
Open in your browser:
```
localhost:5000
```
Currently, this was tested on Google Chrome.

## Unit testing using PyTest
Run `py.test` in the main folder.

## TODO
- [x] Two tabs, two different users.
- [ ] Allow registered users only.
- [ ] Handle `/stock` messages.
- [ ] Decoupled bot.
- [ ] Parse received CSV.
- [x] Order messages by timestamps.
- [ ] Show only 50 last messages.
- [x] Unit testing.
- [ ] Stock command won't be saved on the database.
- [x] Simple front-end.

## Branches
`master` branch contains the latest working chatroom. `develop` branch is experimental.

Additional branches have work-in-progress features. Please do pull requests (PR) to `develop` first.