import argparse
from board import Board


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solve A-Puzzle-A-Day')
    parser.add_argument('--month', '-m', dest='month', type=int, choices=range(1, 13),
                        metavar="[1-12]", help='month to find')
    parser.add_argument('--day', '-d', dest='day', type=int, choices=range(1, 31),
                        metavar="[1-31]", help='day to find')
    parser.add_argument('--force', '-f', dest='force', action="store_true",
                        help='force search for invalid date')
    parser.add_argument('--all', '-a', dest='all', action="store_true",
                        help='search all solutions')
    args = parser.parse_args()
    if not ((args.day and args.month) or args.all):
        raise Exception(f"Use --all or give me a date with --month and --day")
    board = Board()
    if args.all:
        #TODO
        pass
    else:
        if args.day > 30 and not args.month in (1, 3, 5, 7, 8, 10, 12) or args.day > 29 and args.month == 2:
            if not args.force:
                raise Exception(f"Invalid combination of day and month ({args.day}, {args.month}): fix it or use --f")
        board.solve(day=args.day, month=args.month)
