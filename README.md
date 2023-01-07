# BBC-SE-Grad-Tech-Interview-2023
BBC Graduate Software Engineer technical interview

This is the repo for my BBC Graduate Software Engineering technical interview.

## Prerequisites

- Python => 3.10
- pip

## Dependencies
This application has dependencies from PyPi that are required for the application to function.
You can run the following command to install the dependencies.

```bash
pip install -r requirements.txt
```

*it's recommended you create a Python virtual environment to run this application*

## Playing the game
A basic playable cmdline game can be started using the following command from the application's root dir.

```bash
python -m app
```
Then follow the onscreen instructions to start the game.

*This application build as a module*

## Unit Tests
This application uses PyTest to for unit testing installed with the dependencies, to run the unit test you can do the
following command.

```bash
pytest tests/
```

*This GitHub repo automatically run tests on Master and PRs to the Master branch, 
configuration for this can be found in `.gihtub/workflows`*



