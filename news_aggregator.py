import argparse
import json
import logging
from pathlib import Path
from datetime import datetime
import os 

import requests
import pandas as pd
from dotenv import load_dotenv
  


# Configuration

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
API_URL = "https://newsapi.org/v2/top-headlines"

DATA_FILE = Path("news.json")
EXPORT_DIR = Path("exports")


# Logging configuration

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)


# Fetch news from NewsAPI

def fetch_news(keyword=None, country="us"):
    """
    Fetch news articles from NewsAPI.
    """

    params = {
        "apiKey": API_KEY,
        "country": country,
        "pageSize": 100
    }

    if keyword:
        params["q"] = keyword

    logger.info("Fetching news from NewsAPI...")

    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if data.get("status") != "ok":
            logger.error(
                "NewsAPI error: %s",
                data.get("message", "Unknown error")
            )
            return []

        articles = data.get("articles", [])

        logger.info("Fetched %d articles.", len(articles))

        return articles

    except requests.exceptions.RequestException as error:
        logger.error("Failed to fetch news: %s", error)
        return []



# Clean article data

def clean_articles(articles):
    """
    Keep only the useful fields from each article.
    """

    cleaned_articles = []

    for article in articles:

        source = article.get("source") or {}

        cleaned_article = {
            "title": article.get("title"),
            "source": source.get("name"),
            "author": article.get("author"),
            "description": article.get("description"),
            "url": article.get("url"),
            "published_at": article.get("publishedAt")
        }

        # Ignore articles without a title
        if not cleaned_article["title"]:
            continue

        cleaned_articles.append(cleaned_article)

    return cleaned_articles



# Remove duplicate articles

def remove_duplicates(articles):
    """
    Remove duplicate articles using their URL.
    """

    unique_articles = []
    seen_urls = set()

    for article in articles:

        url = article.get("url")

        if url and url in seen_urls:
            continue

        if url:
            seen_urls.add(url)

        unique_articles.append(article)

    logger.info(
        "Removed duplicates. %d unique articles remain.",
        len(unique_articles)
    )

    return unique_articles



# Save articles to JSON

def save_to_json(articles):
    """
    Save articles to news.json.
    """

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            articles,
            file,
            indent=4,
            ensure_ascii=False
        )

    logger.info(
        "Saved %d articles to %s",
        len(articles),
        DATA_FILE
    )



# Load articles from JSON

def load_from_json():
    """
    Load articles from news.json.
    """

    if not DATA_FILE.exists():
        logger.error(
            "news.json does not exist. Run --fetch first."
        )
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        logger.error("news.json contains invalid JSON.")
        return []



# Filter articles

def filter_articles(
    articles,
    source=None,
    keyword=None,
    date=None
):
    """
    Filter articles by source, keyword, and date.
    """

    filtered = articles

    # Filter by source
    if source:
        filtered = [
            article
            for article in filtered
            if article.get("source")
            and source.lower() in article["source"].lower()
        ]

    # Filter by keyword
    if keyword:
        keyword_lower = keyword.lower()

        filtered = [
            article
            for article in filtered
            if keyword_lower in (
                article.get("title") or ""
            ).lower()
            or keyword_lower in (
                article.get("description") or ""
            ).lower()
        ]

    # Filter by date
    if date:
        filtered = [
            article
            for article in filtered
            if (
                article.get("published_at")
                and article["published_at"].startswith(date)
            )
        ]

    return filtered



# Display articles

def display_articles(articles):
    """
    Display news articles in the terminal.
    """

    if not articles:
        print("\nNo articles found.")
        return

    print("\n" + "=" * 70)
    print(f"Found {len(articles)} article(s)")
    print("=" * 70)

    for number, article in enumerate(articles, start=1):

        print(f"\n{number}. {article.get('title')}")
        print(f"   Source: {article.get('source')}")
        print(f"   Author: {article.get('author')}")
        print(f"   Date: {article.get('published_at')}")
        print(f"   URL: {article.get('url')}")

        description = article.get("description")

        if description:
            print(f"   Description: {description}")



# Export to CSV

def export_csv(articles):
    """
    Export articles to CSV.
    """

    if not articles:
        logger.warning("No articles to export.")
        return

    EXPORT_DIR.mkdir(exist_ok=True)

    dataframe = pd.DataFrame(articles)

    output_file = EXPORT_DIR / "news.csv"

    dataframe.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )

    logger.info(
        "CSV file created: %s",
        output_file
    )



# Export to Excel

def export_excel(articles):
    """
    Export articles to Excel.
    """

    if not articles:
        logger.warning("No articles to export.")
        return

    EXPORT_DIR.mkdir(exist_ok=True)

    dataframe = pd.DataFrame(articles)

    output_file = EXPORT_DIR / "news.xlsx"

    dataframe.to_excel(
        output_file,
        index=False,
        engine="openpyxl"
    )

    logger.info(
        "Excel file created: %s",
        output_file
    )



# Command-line arguments

def parse_arguments():

    parser = argparse.ArgumentParser(
        description="News Aggregator CLI"
    )

    parser.add_argument(
        "--fetch",
        action="store_true",
        help="Fetch latest news from NewsAPI"
    )

    parser.add_argument(
        "--keyword",
        type=str,
        help="Filter news by keyword"
    )

    parser.add_argument(
        "--source",
        type=str,
        help="Filter news by source"
    )

    parser.add_argument(
        "--date",
        type=str,
        help="Filter news by date (YYYY-MM-DD)"
    )

    parser.add_argument(
        "--export",
        choices=["csv", "excel"],
        help="Export filtered news to CSV or Excel"
    )

    return parser.parse_args()



# Main program

def main():

    args = parse_arguments()

    # Fetch news
    if args.fetch:

        articles = fetch_news(
            keyword=args.keyword
        )

        articles = clean_articles(articles)

        articles = remove_duplicates(articles)

        save_to_json(articles)

    else:
        articles = load_from_json()

    # Apply filters
    filtered_articles = filter_articles(
        articles,
        source=args.source,
        keyword=args.keyword,
        date=args.date
    )

    # Display results
    display_articles(filtered_articles)

    # Export
    if args.export == "csv":
        export_csv(filtered_articles)

    elif args.export == "excel":
        export_excel(filtered_articles)



# Program entry point

if __name__ == "__main__":
    main()