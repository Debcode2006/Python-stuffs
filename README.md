# Python-stuffs

A small collection of Python utility scripts and demos created for learning and quick automation tasks. Each script is standalone and uses only the Python standard library.

## Projects

### 1) Hangman.py
- Simple console Hangman game (interactive).
- Usage: Run the script and follow on-screen prompts to guess letters until the word is solved or attempts run out.

### 2) StockPortfolioTracker.py
- Lightweight portfolio tracker using hardcoded stock prices.
- Features:
	- User inputs stock symbols and quantities.
	- Uses a predefined dictionary of stock prices to calculate per-stock and total portfolio value.
	- Optionally saves results to a timestamped CSV file.
- Run:
```powershell
python StockPortfolioTracker.py
```
Example flow:
- Enter symbols from the available list (e.g., `AAPL`, `TSLA`).
- Enter quantities as integers.
- Type `done` to finish and view the summary.

### 3) BasicChatbot.py
- A rule-based chatbot that replies to simple inputs like `hello`, `how are you`, and `bye`.
- Case-insensitive matching and a default fallback response for unrecognized inputs.
- Run:
```powershell
python BasicChatbot.py
```

### 4) TaskAutomation.py
- Extracts email addresses from a text file using regular expressions and writes them to a timestamped output file.
- Features:
	- Deduplicates results while preserving order.
	- Produces a human-readable `.txt` file with extraction timestamp and count.
- Run:
```powershell
python TaskAutomation.py
```
Then provide the path to your input `.txt` file when prompted.


## Common notes
- Python: These scripts target Python 3.6+ and use only standard-library modules (no external dependencies required).
- Encoding: File read/write operations use UTF-8 encoding.

## Examples
- To run any script from the project root on Windows PowerShell:
```powershell
cd 'd:\Projects\CodeAlpha'
python StockPortfolioTracker.py
```

## Contributing / Extending
- These are intentionally small and easy-to-extend examples. Feel free to:
	- Add more stocks/prices to `StockPortfolioTracker.py` or wire an API to fetch live prices.
	- Expand `BasicChatbot.py` with pattern matching or integrate NLP libraries.
	- Improve `TaskAutomation.py` to accept multiple formats or to scan directories.

## License
- MIT-style: feel free to reuse and adapt.

---
## Author : Debcode2006
