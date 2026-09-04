def HammingDistance(p, q):
    """Calculate the Hamming distance between two strings p and q."""
    return sum(1 for x, y in zip(p, q) if x != y)

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    # Step 1:k is defined as the length of the Pattern
    Pattern = "TAGCTT"
    k = len(Pattern)
    
    # Step 2: Initialize the total distance to 0
    distance = 0
    
    # Step 3：Traverse each string in the Dna list
    for Text in Dna:
        # Initialize local HammingDistance into infinity (float('inf'))
        min_hamming = float('inf')
        
        # Step 4：Use a sliding window of length 4 to traverse the Text string
        for i in range(len(Text) - k + 1):
            Pattern_prime = Text[i:i+k]
            
            # Calculate the Hamming distance between Pattern and the current substring Pattern_prime
            current_hamming = HammingDistance(Pattern, Pattern_prime)
            
            # If the current Hamming distance is less than the minimum found so far, update min_hamming
            if min_hamming > current_hamming:
                min_hamming = current_hamming
                
        # Step 5：After traversing the entire Text string, add the minimum Hamming distance found to the total distance
        distance = distance + min_hamming
        
    # Step 6：Return the total distance after processing all strings in the Dna list
    return distance

if __name__ == "__main__":
    # We use an example pattern and a list of DNA strings to demonstrate the function
    example_dna = ["AAGATACCC"]
    
    # Execute the function and print the result
    total_dist = DistanceBetweenPatternAndStrings(example_pattern, example_dna)
    print(f"When the target pattern is {example_pattern} ,then, the total distance with {example_dna} : {total_dist}")


