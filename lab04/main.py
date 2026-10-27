import sys

from stats import average_by_city, read_valid, warmest_city


def main() -> None:
    lines = sys.stdin.read().splitlines()

    non_empty = [line for line in lines if line]
    records = read_valid(lines)
    skipped = len(non_empty) - len(records)

    print(len(records))
    print(skipped)

    if records:
        avgs = average_by_city(records)
        best = warmest_city(records)
        print(f"{avgs[best]:.1f}")
    else:
        print("0.0")


if __name__ == "__main__":
    main()
