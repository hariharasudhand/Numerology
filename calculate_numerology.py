import requests

def calculate_numerology(vrn):
    alphabet_values = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
    }

    vrn_letters = ''.join(filter(str.isalpha, vrn.upper()))
    numerology_value = sum(alphabet_values[char] for char in vrn_letters)

    while numerology_value > 9:
        numerology_value = sum(int(digit) for digit in str(numerology_value))

    return numerology_value

def get_local_prediction(numerology_value):
    predictions = {
        1: "Leadership qualities. Independent and original thinker.",
        2: "Cooperative and diplomatic. Sensitive and intuitive.",
        3: "Creative and expressive. Socially active and optimistic.",
        4: "Practical and disciplined. Hardworking and dependable.",
        5: "Adventurous and versatile. Freedom-loving and adaptable.",
        6: "Nurturing and responsible. Compassionate and harmonious.",
        7: "Analytical and introspective. Spiritual and philosophical.",
        8: "Ambitious and authoritative. Materialistic and disciplined.",
        9: "Humanitarian and compassionate. Idealistic and visionary."
    }
    return predictions.get(numerology_value, "Numerology prediction not available.")

def get_numerology_prediction(number, rapidapiKey):
    url = "https://numerology2.p.rapidapi.com/names"
    querystring = {"number": number}
    headers = {
        'x-rapidapi-host': "numerology2.p.rapidapi.com",
        'x-rapidapi-key': rapidapiKey
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    return data

def main():
    ch = int(input("Enter 1 if you want Real Time Predictions from RapidAPI: "))
    vrn = input("Enter the Vehicle Registration Number: ")
    numerology_value = calculate_numerology(vrn)
    print(f"The numerology value of the Vehicle Registration Number {vrn} is {numerology_value}")

    if ch == 1:
        api_key = input("Enter Rapid API Key: ")
        prediction = get_numerology_prediction(numerology_value, api_key)
        print("Numerology prediction from RapidAPI:", prediction)
    else:
        prediction = get_local_prediction(numerology_value)
        print("Numerology prediction:", prediction)

if __name__ == "__main__":
    main()
