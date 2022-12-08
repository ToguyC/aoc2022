import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", "-d", default=0)
    parser.add_argument("--part", "-p", default=1)
    args = parser.parse_args()

    day = f"day{args.day:02}"
    part = f"part{args.part}"

    try:
        part = getattr(__import__(day, fromlist=[part]), part)
        part.main()
    except:
        pass
