is_magician = False
is_expert = True

# Check if magician AND expert: "you are a master magician!"
if is_magician and is_expert:
    print("you are a master magician!")

# Check if magician but not expert: "At leat you're getting there"
elif is_magician and not(is_expert):
    print("At leat you're getting there")

# Check if you are not a magician: "You need magic powers!"
elif not is_magician:
    print("You need magic powers!")
