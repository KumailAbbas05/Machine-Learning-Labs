from sklearn.model_selection import KFold

items = ["a", "b", "c", "d", "e", "f", "g", "h"]

kf = KFold(n_splits=4)

fold_number = 1

for train_positions, test_positions in kf.split(items):
    print("Fold", fold_number)
    print("Train positions:", train_positions)
    print("Test positions:", test_positions)

    tested_items = [items[i] for i in test_positions]
    print("Tested items:", tested_items)
    print()

    fold_number += 1
