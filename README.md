# 📰 News Aggregator CLI

A simple **command-line News Aggregator** built with Python that fetches the latest headlines from **NewsAPI**, cleans and stores the data in JSON, provides filtering options, removes duplicate articles, and exports the results to **CSV or Excel**.

This project is designed as a practical Python project combining **API integration, data processing, CLI development, JSON storage, and CSV/Excel automation**.

---

## 🚀 Features

* 📰 Fetch latest news using **NewsAPI**
* 🔍 Filter news by:

  * Keyword
  * Source
  * Date
* 🧹 Clean and organize article data
* ♻️ Remove duplicate articles using article URLs
* 💾 Store collected news in `news.json`
* 📊 Export news to **CSV**
* 📗 Export news to **Excel**
* 📝 Logging for errors and program activities
* 💻 Easy-to-use command-line interface

---

## 🛠️ Technologies Used

* **Python**
* **NewsAPI**
* **Requests** – API requests
* **Pandas** – data processing and CSV/Excel export
* **OpenPyXL** – Excel file creation
* **python-dotenv** – environment variable management
* **Argparse** – command-line arguments
* **JSON** – data storage

---

## 📂 Project Structure

```text
news_aggregator/
│
├── news_aggregator.py     # Main Python program
├── news.json              # Stored news data
├── .env                   # API key (DO NOT upload)
├── .gitignore             # Files excluded from Git
│
├── exports/
│   ├── news.csv           # Exported CSV file
│   └── news.xlsx          # Exported Excel file
│
└── README.md              # Project documentation
```


## 🔍 Filtering News

### Filter by Keyword

```bash
python news_aggregator.py --fetch --keyword technology
```

You can also filter already stored news:

```bash
python news_aggregator.py --keyword technology
```

---

### Filter by Source

```bash
python news_aggregator.py --source CNN
```

This displays articles from the specified news source.

---

### Filter by Date

Use the date format:

```text
YYYY-MM-DD
```

Example:

```bash
python news_aggregator.py --date 2026-10-07
```

---

## 📊 Export News

### Export to CSV

```bash
python news_aggregator.py --export csv
```

The CSV file will be created inside:

```text
exports/news.csv
```

### Export to Excel

```bash
python news_aggregator.py --export excel
```

The Excel file will be created inside:

```text
exports/news.xlsx
```

---

## 🔎 Combine Filters

Multiple filters can be used together.

For example:

```bash
python news_aggregator.py --keyword technology --source CNN --export excel
```

This filters the stored articles by keyword and source and exports the results to Excel.

You can also fetch and filter at the same time:

```bash
python news_aggregator.py --fetch --keyword technology --export csv
```

---

## 🧹 Deduplication

The program automatically removes duplicate articles using their **article URL**.

For example, if the same article appears multiple times with the same URL, only one copy will be stored.

This helps keep the collected dataset clean and organized.

---

## 💾 Data Storage

The collected news is stored in:

```text
news.json
```

Each article contains useful information such as:

```json
{
    "title": "Example News Headline",
    "source": "Example News",
    "author": "Author Name",
    "description": "News description...",
    "url": "https://example.com/news",
    "published_at": "2026-10-07T10:00:00Z"
}
```

---

## 📤 Exported Data

The project supports two export formats:

| Format | File                | Purpose                            |
| ------ | ------------------- | ---------------------------------- |
| JSON   | `news.json`         | Store and reuse collected news     |
| CSV    | `exports/news.csv`  | Data analysis and sharing          |
| Excel  | `exports/news.xlsx` | Reporting and spreadsheet analysis |

---

## 📝 Logging

The project uses Python's built-in `logging` module to display useful information and errors.

Example:

```text
INFO: Fetching news from NewsAPI...
INFO: Fetched 20 articles.
INFO: Removed duplicates. 18 unique articles remain.
INFO: Saved 18 articles to news.json
```

If there is an API or network problem, an error message is displayed instead of crashing the program.

---

## 🧩 Main Functions

The project is divided into several functions:

### `fetch_news()`

Fetches news articles from NewsAPI.

### `clean_articles()`

Keeps only the required article information.

### `remove_duplicates()`

Removes duplicate articles based on their URLs.

### `save_to_json()`

Stores articles in `news.json`.

### `load_from_json()`

Loads previously saved articles.

### `filter_articles()`

Filters articles by source, keyword, and date.

### `display_articles()`

Displays news articles in the terminal.

### `export_csv()`

Exports filtered articles to CSV.

### `export_excel()`

Exports filtered articles to Excel.

### `parse_arguments()`

Handles command-line arguments.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. To collect news headlines automatically using an API.
2. To provide an easy command-line interface for searching and filtering news.
3. To store news data for later use.
4. To remove duplicate articles from collected data.
5. To automate CSV and Excel report generation.
6. To practice API integration and Python data processing.

---

## 🔮 Future Improvements

Possible future improvements include:

* 🌐 Add more news sources
* 🗄️ Add SQLite database support
* 🔎 Add advanced search and sorting
* 🕐 Add automatic scheduled news collection
* 📰 Add web scraping alongside NewsAPI
* 🖥️ Build a graphical or web interface
* 📈 Add news statistics and visualizations
* 🌍 Allow users to select different countries

---

## 📚 Learning Outcomes

Through this project, I practiced:

* Python programming
* REST API integration
* Command-line application development
* JSON data handling
* Data cleaning
* Data filtering
* Duplicate removal
* Pandas
* CSV and Excel automation
* Environment variables and API key security
* Error handling and logging
* Git and GitHub project management

---

## 👩‍💻 Author

Anamika Dhakal

BICTE | Python Programmer

This project was developed as a Python learning project to practice **API integration, data processing, automation, and command-line application development**.

