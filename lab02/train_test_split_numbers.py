from sklearn.model_selection import train_test_split

numbers = list(range(1, 21))

train, test = train_test_split(
    numbers,
    test_size=0.25,
    random_state=0
)

print("Train list:", train)
print("Test list:", test)

print("Train count:", len(train))
print("Test count:", len(test))
