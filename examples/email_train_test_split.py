from sklearn.model_selection import train_test_split

emails = [
    "e1", "e2", "e3", "e4", "e5",
    "e6", "e7", "e8", "e9", "e10"
]

train_emails, test_emails = train_test_split(
    emails,
    test_size=0.2,
    random_state=0
)

print("Train emails:", train_emails)
print("Test emails:", test_emails)
