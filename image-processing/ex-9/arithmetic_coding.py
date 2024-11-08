import random

def calculate_relative_frequency(lst):
  freq = {}
  total = len(lst)

  for item in lst:
    freq[item] = freq.get(item, 0) + 1

  for item, count in freq.items():
    freq[item] = count / total

  return freq

def calculate_cumulative_prob(probabilities):
    cumulative_prob = {}
    cumulative = 0.0
    for symbol, prob in probabilities.items():
        cumulative_prob[symbol] = (cumulative, cumulative + prob)
        cumulative += prob
    return cumulative_prob

def encode_sequence(data, cumulative_prob):
    low = 0.0
    high = 1.0
    ranges = []
    for symbol in data:
        range_ = high - low
        high = low + range_ * cumulative_prob[symbol][1]
        
        low = low + range_ * cumulative_prob[symbol][0]
        ranges.append((low, high))
    key = random.uniform(ranges[-1][0],ranges[-1][1])
    return key,ranges

def decode_value(encoded_value, length, cumulative_prob):
    decoded_data = []
    low = 0.0       
    high = 1.0

    for _ in range(length):
        range_ = high - low
        code = (encoded_value - low) / range_

        for symbol, (sym_low, sym_high) in cumulative_prob.items():
            # print(sym_low <= code < sym_high,symbol) here we get the correct items
            if sym_low <= code < sym_high:
                decoded_data.append(symbol)
                high = low + range_ * sym_high
                low = low + range_ * sym_low
                break

    return decoded_data


data = list(map(int,input("enter the sequence of the images (between 0to 255): ").split(" ")))

probabilities = calculate_relative_frequency(data)
# print(probabilities) 


cumulative_prob = calculate_cumulative_prob(probabilities)
print(f"cumulative probability : \n {cumulative_prob}")

encoded_value,ranges = encode_sequence(data, cumulative_prob)

print(f"Encoded value: {encoded_value}\n")
# print(f"ranges : {ranges}\n")

decoded_data = decode_value(encoded_value, len(data), cumulative_prob)

for i, symbol in enumerate(data):
    range_ = cumulative_prob[symbol]
    # print(f"Range for '{symbol}': {range_}")

# print(f"Decoded sequence: {decoded_data}")