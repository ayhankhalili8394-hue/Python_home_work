songs = [
    ["Believer", "Imagine Dragons"],
    ["Shape of You", "Ed Sheeran"],
    ["Perfect", "Ed Sheeran"],
    ["Believer", "Other Singer"],
    ["Thunder", "Imagine Dragons"]
]

song_name = input("Enter the song name: ")
singer_name = input("Enter the singer name: ")

results = []

for song in songs:
    if song_name == song[0] or singer_name == song[1]:
        results.append(song)

if results:
    print("Search results:")
    for song in results:
        print("Song:", song[0], "| Singer:", song[1])
else:
    print("Sorry, no matching songs were found.")
