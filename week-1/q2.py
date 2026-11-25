user_preferences = {
    "theme": "dark",
    "notifications": True,
    "language": "en-US",
    "font_size": 14
}

currency = user_preferences.get("currency", "USD")
print("Currency:", currency)

user_preferences["font_size"] = 16
user_preferences.pop("notifications")

print("Updated Preferences:")
for key, value in user_preferences.items():
    print(f"{key}: {value}")
