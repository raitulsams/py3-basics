mydict = {
    "name": "Sams",
    "age": 26,
    "hobby": ["Online games", "New Surfing", "Reading"],
    "favourite_color": [{
        "dark": "Blue"
    }, {
        "dark": "Blue"
    }, ]

}

fav_color = mydict["favourite_color"]

print((fav_color[1]))
print(mydict.get("age"))

print(f"All keys value: {mydict.keys()}")
