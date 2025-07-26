# fetch_publications.py
from pyzotero import zotero
import yaml
import re # For regex to clean up DOIs/PMIDs
import os

# --- Zotero API Configuration ---
# !!! IMPORTANT: Replace with your actual Zotero ID and API Key !!!
# Fetch from environment variables, which GitHub Actions will set from your secrets
# For local testing, you can temporarily hardcode or set these env vars in your shell

# If using a User Library:
library_id = os.environ.get('ZOTERO_USER_ID') # Get user/group ID from environment
library_type = 'group' # or 'user' - keep this as it is, or get from env if needed
api_key = os.environ.get('YOUR_ZOTERO_API_KEY')   # Get API key from environment

# If fetching from a specific collection (optional, set to None if not using):
collection_key = None

# --- Output File ---
output_yaml_file = '_data/publications.yml'

# --- Validate Configuration ---
if not library_id:
    print("Error: ZOTERO_USER_ID environment variable not set. Please configure your GitHub Secret or local environment.")
    exit(1)
if not api_key:
    print("Warning: ZOTERO_API_KEY environment variable not set. Proceeding without API key (only for truly public libraries).")
    # You might want to exit here if you absolutely require the key.
    # For a public library where you've chosen to use a key for robustness, this warning is acceptable.
    # If the Zotero API then rejects without the key, the subsequent `zot.items()` call will fail.

# --- Initialize Zotero API ---
try:
    # Use zotero.Zotero to access the class from the imported module
    zot = zotero.Zotero(library_id, library_type, api_key)
    print("Successfully connected to Zotero API.")
except Exception as e:
    print(f"Error connecting to Zotero API: {e}")
    print("Please check your library_id, library_type, and api_key.")
    exit(1)

# --- Fetch Items ---
items = []
try:
    if collection_key:
        items = zot.collection_items(collection_key)
        print(f"Fetched {len(items)} items from collection '{collection_key}'.")
    else:
        items = zot.everything(zot.items())
        print(f"Fetched {len(items)} items from library.")
except Exception as e:
    print(f"Error fetching items from Zotero: {e}")
    exit()

# --- Process and Format Data ---
publications = []
for item in items:
    # Filter for "Journal Article", "Conference Paper", "Book Section", "Book", etc.
    # Adjust 'itemType' as per your needs. 'publicationTitle' is common for articles.
    if item['data']['itemType'] in ['journalArticle', 'conferencePaper', 'bookSection', 'book']:
        data = item['data']

        # Extract basic info
        title = data.get('title', 'No Title')
        authors = []
        if 'creators' in data:
            for creator in data['creators']:
                if creator['creatorType'] in ['author', 'editor']:
                    if 'lastName' in creator and 'firstName' in creator:
                        authors.append(f"{creator['firstName']} {creator['lastName']}")
                    elif 'lastName' in creator: # Sometimes only last name is available
                        authors.append(creator['lastName'])
                    elif 'name' in creator: # For organizations or if structured names are missing
                        authors.append(creator['name'])
        authors_str = ", ".join(authors)

        date = data.get('date', '')
        year = ''
        if date:
            # Attempt to extract year from date field, handling various formats
            match_year = re.search(r'\b\d{4}\b', date)
            if match_year:
                year = match_year.group(0)
            else: # Fallback for just year
                year = date.split('-')[0] # Assumes YYYY-MM-DD or similar

        journal = data.get('publicationTitle', data.get('series', '')) # For journal articles, books

        # Extract DOI and PMID, and format into links
        doi = data.get('DOI', '')
        doi_link = ''
        if doi:
            # Clean up DOI (remove 'doi:' prefix if present)
            doi = doi.replace('doi:', '').strip()
            doi_link = f"https://doi.org/{doi}"

        pubmed_id = data.get('PMID', '')
        pubmed_link = ''
        if pubmed_id:
            # PMID is usually just the number, but ensure it's clean
            pubmed_id = re.sub(r'\D', '', pubmed_id) # Remove non-digits
            if pubmed_id:
                pubmed_link = f"https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}/"

        publications.append({
            'title': title,
            'authors': authors_str,
            'year': year,
            'journal': journal,
            'doi': doi,
            'doi_link': doi_link,
            'pubmed_id': pubmed_id,
            'pubmed_link': pubmed_link,
            'item_key': item['data']['key'] # Zotero item key for direct linking if needed
        })

# Sort publications by year in descending order
publications.sort(key=lambda x: x['year'], reverse=True)

# --- Write to YAML file ---
try:
    # Create _data directory if it doesn't exist
    import os
    os.makedirs(os.path.dirname(output_yaml_file), exist_ok=True)

    with open(output_yaml_file, 'w', encoding='utf-8') as f:
        yaml.dump(publications, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    print(f"Successfully generated {output_yaml_file} with {len(publications)} publications.")
except Exception as e:
    print(f"Error writing YAML file: {e}")