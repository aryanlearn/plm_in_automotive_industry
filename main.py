"""Entry point.

  python main.py       # auto demo
  python main.py cli   # interactive menu
"""

import sys

from plm.demo import run_demo


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1].lower() == "cli":
        from plm.cli import run_cli

        run_cli()
    else:
        run_demo()


if __name__ == "__main__":
    main()
