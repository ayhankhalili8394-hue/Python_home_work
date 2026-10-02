
songs = [
    ["Believer", "Imagine Dragons"],
    ["Shape of You", "Ed Sheeran"],
    ["Perfect", "Ed Sheeran"],
    ["Believer", "Other Singer"]
]

song_name = input("Enter the song name: ")
singer_name = input("Enter the singer name: ")

found = False

for song in songs:
    if song[0] == song_name and song[1] != singer_name:
        songs.remove(song)
        songs.insert(0, song)
        print("A song with the same name but a different singer was found!")
        print("Song:", song[0])
        print("Singer:", song[1])
        found = True
        break

if not found:
    print("No song with the same name and a different singer was found.")

print("Updated song list:")
for song in songs:
    print(song)
