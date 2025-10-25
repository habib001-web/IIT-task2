import json
import urllib.request
import sys

def fetch_sec_data(cik):
    """Fetch SEC data for a given CIK"""
    url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/dei/EntityCommonStockSharesOutstanding.json"
    
    # SEC requires a User-Agent header
    req = urllib.request.Request(
        url,
        headers={
            'User-Agent': 'AMD Stock Analysis Tool contact@example.com'
        }
    )
    
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    
    return data

def process_data(data):
    """Process SEC data to extract max and min shares after 2020"""
    entity_name = data.get('entityName', '')
    
    # Get shares data
    shares = data.get('units', {}).get('shares', [])
    
    # Filter for fy > "2020" and numeric val
    filtered = []
    for entry in shares:
        if 'fy' in entry and 'val' in entry:
            fy = str(entry['fy'])
            val = entry['val']
            if fy > "2020" and isinstance(val, (int, float)):
                filtered.append({'val': val, 'fy': fy})
    
    if not filtered:
        raise ValueError("No valid data found for fiscal years > 2020")
    
    # Find max and min
    max_entry = max(filtered, key=lambda x: x['val'])
    min_entry = min(filtered, key=lambda x: x['val'])
    
    result = {
        'entityName': entity_name,
        'max': {
            'val': max_entry['val'],
            'fy': max_entry['fy']
        },
        'min': {
            'val': min_entry['val'],
            'fy': min_entry['fy']
        }
    }
    
    return result

def main():
    cik = "0000002488"
    
    print(f"Fetching data for CIK {cik}...")
    raw_data = fetch_sec_data(cik)
    
    print("Processing data...")
    result = process_data(raw_data)
    
    print("Saving to data.json...")
    with open('data.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    print("Done!")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()