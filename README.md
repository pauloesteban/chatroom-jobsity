# Chatroom

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

## TODO
- [x] Two tabs, two different users.
- [ ] Allow registered users only.
- [ ] Handle `/stock` messages.
- [ ] Decoupled bot.
- [ ] Parse received CSV.
- [ ] Ordering messages.
- [ ] Unit testing.
- [ ] Stock command won't be saved on the database.
- [x] Simple front-end.

## Branches
`master` branch contains the latest working chatroom. `develop` branch is experimental and have work in progress features.