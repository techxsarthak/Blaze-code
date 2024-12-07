#please install requests first by clicking install module in ide
import requests

BASE_URL = "https://restcountries.com/v3.1/"

def get_country_by_name(country_name):
    """Fetch country details by name."""
    try:
        response = requests.get(f"{BASE_URL}name/{country_name}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching country data: {e}")
        return None

def display_country_info(country_data):
    """Display country information in a user-friendly format."""
    if not country_data:
        print("No data available.")
        return

    country = country_data[0]  # Access the first matching country
    name = country.get("name", {}).get("common", "Unknown")
    capital = country.get("capital", ["Unknown"])[0]
    region = country.get("region", "Unknown")
    population = country.get("population", "Unknown")
    languages = ", ".join(country.get("languages", {}).values())
    currencies = ", ".join([f"{v['name']} ({v['symbol']})" for v in country.get("currencies", {}).values()])

    print("\n--- Country Information ---")
    print(f"Name: {name}")
    print(f"Capital: {capital}")
    print(f"Region: {region}")
    print(f"Population: {population}")
    print(f"Languages: {languages}")
    print(f"Currencies: {currencies}")

def main():
    print("Welcome to the Country Information Finder!")
    while True:
        country_name = "india"
        if country_name.lower() == "exit":
            print("Goodbye!")
            break

        country_data = get_country_by_name(country_name)
        if country_data:
            display_country_info(country_data)
        else:
            print("No matching country found. Please try again.")

if __name__ == "__main__":
    main()
