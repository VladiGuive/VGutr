from pprint import pprint
def main() -> None:
    from parser import load_toml
    monitors, integrations = load_toml()
    for monitor in monitors:
        pprint(vars(monitor))


if __name__ == "__main__":
    main()
