import sys
import json

def main():
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: JsonRead.py <path_to_json_file> <json_query>")
        sys.exit(1)

    # Get the file path and query from command line arguments
    file_path = sys.argv[1]
    json_query = sys.argv[2]

    try:
        # Open and read the JSON file
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        # Evaluate the query dynamically using Python syntax
        try:
            result = eval(f"data{json_query}")
            # Print the result to console
            print(json.dumps(result, indent=4))
        except (KeyError, IndexError, TypeError, NameError) as e:
            print(f"Error in JSON query: {e}")
            sys.exit(1)

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file at {file_path} is not valid JSON.")
        sys.exit(1)

if __name__ == "__main__":
    main()
