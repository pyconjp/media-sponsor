"""
$ python3.10 list_example.py
entrée='awesome meat dish', side='fabulous side'

ref: https://youtu.be/ggPJLwIbbyY?t=1080
"""

meal = ["awesome meat dish", "fabulous side"]

match meal:
    case entrée, side:
        print(f"{entrée=}, {side=}")
