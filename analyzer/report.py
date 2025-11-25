from typing import List, Dict


def print_report(results: List[Dict]):
    total = len(results)
    success = sum(1 for r in results if r["status"] and r["status"] < 400)

    print("\n--- Web Performance Report ---")
    print(f"Total URLs: {total}")
    print(f"Successful: {success}")
    print(f"Failed: {total - success}")

    print("\nDetails:")
    for r in results:
        status = r.get("status")
        t = round(r["time"], 4)
        print(f"{r['url']} | status={status} | time={t}s")
