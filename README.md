# Auto Temperature Recorder

### Disclaimer

This tool does not encourage non-compliance of NUS policies - it merely automates the process of submitting temperatures for the day.

### Quickstart

1. Figure out your Chrome version by clicking on the menu button at the top right corner > Help > About Chrome.
2. Download the appropriate Chrome drivers from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
3. Place your Chrome driver in the root of this directory as `chromedriver.exe`. If you are using another OS, you have to edit the source code directly to use your Chrome driver.
4. Type in `source .venv/bin/activate` to activate the virtual environment.
5. Create a new `.env` file, and key in your credentials in the `.env` file as shown in `.env.example`. Temperature readings are optional. If you leave them blank, it will record a random temperature between 36.1 to 36.9.
6. Run `python record.py` and enjoy the 30 seconds that you saved! Alternatively, you can run `python record.py --manual` to key in your temperatures manually. In the manual mode, temperatures that are in your `.env` file are ignored.
