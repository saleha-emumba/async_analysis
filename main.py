import argparse
import asyncio
from analyzer.loader import load_urls
from analyzer.fetcher import fetch_all
from analyzer.report import print_report


def build_parser():
    p = argparse.ArgumentParser(description="Async Web Performance Analyzer")
    p.add_argument("file", help="Path to URL list JSON file")
    p.add_argument("--limit", type=int, default=10, help="Concurrency limit")
    return p


def cli():
    parser = build_parser()
    args = parser.parse_args()

    urls = load_urls(args.file)
    results = asyncio.run(fetch_all(urls, args.limit))
    print_report(results)


if __name__ == "__main__":
    cli()
