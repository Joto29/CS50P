SHOWS = ["Avatar: The Last Airbender",
         "ben 10",
         "  arthur",
         "Spongebob   squarepants",
         "phineas and ferb",
         "   Kim possible",
         "JIMMY NEUTRON",
         "the proud family"]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
    
    print(', '.join(cleaned_shows))

main()