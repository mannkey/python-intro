# Most usefull commands WRT python

> This document is collection of helpful commands which we can use as cli

## Run Function from CLI

To test an individual function from the command line, we can use the python flag `-c` which is `command` we can import and run a function from with in cli.

```bash
    python -c "from utils.date_utils import get_today_date; get_today_date()"
```
Arguments can also be passed to the function. To know more about this refer [upvoted stack answer] (https://stackoverflow.com/a/3987113).
