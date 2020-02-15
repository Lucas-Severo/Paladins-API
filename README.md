# Paladins API wrapper

This project is a paladins-api wrapper using python and flask

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requeriments.txt
```

## Configuration

First of all, it's necessary the devId and sessionId, that you can obtain through the [Hirez form](https://fs12.formsite.com/HiRez/form48/secure_index.html)

then, you need to fill in the blank fields in the app.py file

```bash
app.py

devId = ""
sessionId = ""
```

## Usage
Now, to run the application:
```
python app.py
```

## Routes
```
/getplayer/player - returns the player info
/getchampions/player - returns the player champions sorted by most played
/getstatus/player - returns the player status
/searchplayers/player - returns all occurrences of a nickname
/getmatches/player - returns the player match history
```

## Contributing
Pull requests are welcome.


## License
[MIT](https://choosealicense.com/licenses/mit/)
