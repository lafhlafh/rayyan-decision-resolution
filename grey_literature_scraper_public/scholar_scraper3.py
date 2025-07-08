from serpapi import GoogleSearch
import pandas as pd
import time

# Function to search Google Scholar using SerpAPI
def search_google_scholar(query, max_results=50):
    print(f"Searching for: {query}")
    
    api_key = "API_KEY"  # Your SerpAPI key
    results = []
    current_start = 0  # Pagination start index

    while len(results) < max_results:
        params = {
            "engine": "google_scholar",
            "q": query,
            "start": current_start,
            "api_key": api_key,
        }

        search = GoogleSearch(params)
        response = search.get_dict()

        # Check for errors
        if "error" in response:
            print(f"Error: {response['error']}")
            break

        # Extract search results
        if "organic_results" in response:
            for result in response["organic_results"]:
                # Extract authors properly
                raw_authors = result.get("publication_info", {}).get("authors", [])
                authors = ", ".join([author.get("name", "") for author in raw_authors]) if raw_authors else "N/A"

                # Extract journal and year
                publication_info = result.get("publication_info", {})
                journal = publication_info.get("publication", "N/A")
                year = publication_info.get("year", "N/A")

                # Clean snippet
                snippet = result.get("snippet", "")
                cleaned_snippet = snippet.encode("utf-8", errors="ignore").decode("utf-8").replace("\n", " ").replace("\r", " ")

                # Append result
                results.append({
                    "Title": result.get("title", ""),
                    "Authors": authors,
                    "Journal": journal,
                    "Year": year,
                    "Citations": result.get("inline_links", {}).get("cited_by", {}).get("total", 0),
                    "URL": result.get("link", ""),
                    "Snippet": cleaned_snippet,
                })
        else:
            print("No results found.")
            break

        # Handle pagination
        if "pagination" in response and "next" in response["pagination"]:
            current_start += 10
        else:
            break

        time.sleep(2)

    return results[:max_results]

# Main function
def main():
    search_terms = (
        "(\"multi-drug resistant\" OR \"multidrug resistant\" OR esbl OR \"extended spectrum betalactamase\" "
        "OR ampc OR cpo OR \"Carbapenem-resistant Acinetobacter baumannii\" OR crab OR \"third generation cephalosporin resistant\" "
        "OR amr OR \"antimicrobial resistance\" OR \"antimicrobial resistant\" OR \"antibiotic resistant\" OR \"antibiotic resistance\") "
        "AND TITLE-ABS-KEY (coliform OR enterobacteria* OR \"e coli\" OR \"k pneumoniae\" OR \"escherichia coli\" "
        "OR \"klebsiella pneumoniae\" OR acinetobacter OR pseudomonas OR \"gram negative\" OR bacteria*) "
        "AND TITLE-ABS-KEY ((\"pregnan*\" OR \"postpartum\" OR \"peripartum\" OR \"postnatal\" OR \"matern*\")) "
        "AND TITLE-ABS-KEY ((\"Angola\" OR \"Bangladesh\" OR \"Benin\" OR \"Bhutan\" OR \"Bolivia\" OR \"Cabo Verde\" OR \"Cape Verde\" "
        "OR \"Cambodia\" OR \"Cameroon\" OR \"Comoros\" OR \"Republic of Congo\" OR \"Congo, Rep.\" OR \"Congo Brazzaville\" "
        "OR \"Côte d’Ivoire\" OR \"Ivory Coast\" OR \"Djibouti\" OR \"Egypt\" OR \"Arab Republic of Egypt\" "
        "OR \"El Salvador\" OR \"Eswatini\" OR \"Swaziland\" OR \"Ghana\" OR \"Haiti\" OR \"Honduras\" OR \"India\" OR \"Indonesia\" "
        "OR \"Iran\" OR \"Islamic Republic of Iran\" OR \"Kenya\" OR \"Kiribati\" OR \"Kyrgyzstan\" OR \"Kyrgyz Republic\" "
        "OR \"Lao PDR\" OR \"Laos\" OR \"Lebanon\" OR \"Lesotho\" OR \"Mauritania\" OR \"Micronesia\" OR \"Federated States of Micronesia\" "
        "OR \"Morocco\" OR \"Myanmar\" OR \"Burma\" OR \"Nepal\" OR \"Nicaragua\" OR \"Nigeria\" OR \"Pakistan\" "
        "OR \"Papua New Guinea\" OR \"PNG\" OR \"Philippines\" OR \"Samoa\" OR \"São Tomé and Príncipe\" OR \"Sao Tome and Principe\" "
        "OR \"Senegal\" OR \"Solomon Islands\" OR \"Sri Lanka\" OR \"Ceylon\" OR \"Tajikistan\" OR \"Tanzania\" "
        "OR \"Timor-Leste\" OR \"East Timor\" OR \"Tunisia\" OR \"Ukraine\" OR \"Uzbekistan\" OR \"Vanuatu\" OR \"Vietnam\" "
        "OR \"Zambia\" OR \"Zimbabwe\" OR \"Albania\" OR \"Algeria\" OR \"Argentina\" OR \"Armenia\" OR \"Azerbaijan\" OR \"Republic of Belarus\" OR \"Belarus\" "
        "OR \"Belize\" OR \"Bosnia-Herzegovina\" OR \"Bosnia and Herzegovina\" OR \"Botswana\" OR \"Brazil\" OR \"China\" OR \"People's Republic of China\" "
        "OR \"Colombia\" OR \"Costa Rica\" OR \"Cuba\" OR \"Dominica\" OR \"Dominican Republic\" OR \"Ecuador\" OR \"Equatorial Guinea\" OR \"Fiji\" "
        "OR \"Gabon\" OR \"Georgia\" OR \"Georgia (Republic)\" OR \"Grenada\" OR \"Guatemala\" OR \"Guyana\" OR \"Jamaica\" OR \"Jordan\" "
        "OR \"Kazakhstan\" OR \"Kosovo\" OR \"Libya\" OR \"Malaysia\" OR \"Maldives\" OR \"Mauritius\" OR \"Mexico\" OR \"Moldova\" OR \"Republic of Moldova\" "
        "OR \"Mongolia\" OR \"Montenegro\" OR \"Namibia\" OR \"Republic of North Macedonia\" OR \"North Macedonia\" OR \"Paraguay\" OR \"Peru\" "
        "OR \"Serbia\" OR \"South Africa\" OR \"Saint Lucia\" OR \"St. Lucia\" OR \"Saint Vincent and the Grenadines\" OR \"St. Vincent and the Grenadines\" "
        "OR \"Suriname\" OR \"Thailand\" OR \"Tonga\" OR \"Turkey\" OR \"Türkiye\" OR \"Turkmenistanp\" OR \"Tuvalu\"))"
    )

    results = search_google_scholar(search_terms, max_results=50)

    output_filename = "serpapi_scholar_middleincome_countries_results.csv"
    df = pd.DataFrame(results)
    df.to_csv(output_filename, index=False, encoding="utf-8")
    print(f"Results saved to {output_filename}")

if __name__ == "__main__":
    main()
