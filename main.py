from agents.discovery_agent import DiscoveryAgent


def main() -> None:
    print("=" * 40)
    print("Elitech AI Product Finder")
    print("=" * 40)

    keyword = input("Enter a product to search for: ").strip()

    if not keyword:
        print("You must enter a product.")
        return

    agent = DiscoveryAgent()
    agent.search(keyword)


if __name__ == "__main__":
    main()