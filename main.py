import json

if __name__ == "__main__":
    with open("data.json", "r") as json_file:
        data = json.load(json_file)

    with open("data.csv", "w") as csv_file:
        # Write CSV header
        headers = data[0].keys()
        csv_file.write(",".join(headers) + "\n")

        # Write CSV rows
        for entry in data:
            row = [str(entry[header]) for header in headers]
            csv_file.write(",".join(row) + "\n")