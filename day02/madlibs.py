name=input("Enter your name: ").strip().title()
place=input("Enter a place: ").strip()
animal=input("Enter an animal: ").strip().lower()
number=int(input("Enter a number: "))
adjective=input("Enter an adjective: ").strip().lower()

story=f"""
Once upon a time, in the land of {place}, there lived a {number} {adjective} {animal} named {name}.
"""
print(story)
print(f"story length: {len(story)} characters")
print(f"shoutong version: {story.upper()}")
