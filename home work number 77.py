songs = [
    ["Believer", "Imagine Dragons"],
    ["Shape of You", "Ed Sheeran"],
    ["Perfect", "Ed Sheeran"],
    ["Believer", "Other Singer"],
    ["Thunder", "Imagine Dragons"]
]

song_name = input("Enter the song name: ")
singer_name = input("Enter the singer name: ")

exact_matches = []
same_song = []
same_singer = []

for song in songs:
    if song[0] == song_name and song[1] == singer_name:
        exact_matches.append(song)
    elif song[0] == song_name:
        same_song.append(song)
    elif song[1] == singer_name:
        same_singer.append(song)

results = exact_matches + same_song + same_singer

if results:
    print("Search results:")

    for song in results:
        print("Song:", song[0], "| Singer:", song[1])
else:
    print("Sorry, no matching songs were found.")
