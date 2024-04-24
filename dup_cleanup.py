#---Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, 
#---some of which are duplicated. 
#---Write a Python function that takes in a list of customer ID's, 
#---removes duplicates, prints each unique id, and returns a set of the unique IDs

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def dup_cleanup(customer_ids):
    clean_set = set()
    for id in customer_ids:
        clean_set.add(id)
    print()    
    print('Here is the SET of unique IDs:')
    print(clean_set)
    print()    
    print('AND here is your "clean" list')
    print('-----------------------------')
    for cust in clean_set:
        print(cust)
    print()

dup_cleanup(customer_ids)