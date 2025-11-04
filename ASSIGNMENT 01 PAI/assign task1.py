transactionLog = [
    {'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_10'},
    {'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_12'},
    {'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_10'},
    {'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_15'},
    {'orderId': 1003, 'customerId': 'cust_Ahmed', 'productId': 'prod_15'},
    {'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_12'},
    {'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_10'},
]

productCatalog = {
    'prod_10': 'Wireless Mouse',
    'prod_12': 'Keyboard',
    'prod_15': 'USB-C Hub',
}

def processTransactions(transactionsList):
    
    customerdata = {}
    for t in transactionsList:
        cust = t['customerId']
        prod = t['productId']
        if cust not in customerdata:
            customerdata[cust] = set()
        customerdata[cust].add(prod)
    return customerdata

def findFrequentPairs(customerdata):
    counts = {}
    for products in customerdata.values():
        productlist = list(products)
        for i in range(len(productlist)):
            for j in range(i + 1, len(productlist)):
                pair = tuple(sorted((productlist[i], productlist[j])))
                if pair not in counts:
                    counts[pair] = 1
                else:
                    counts[pair] += 1
               
    return counts

def getRecommendations(targetProductID, frequentPairs):
    recommendations = {}
    for (p1, p2), count in frequentPairs.items():
        if targetProductID in (p1, p2):
            other = p2 if p1 == targetProductID else p1
            recommendations[other] = count
    
    sortedrecomm = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sortedrecomm
  
def generateReport(targetProductID, recommendations, catalog):
    print(f"\nRecommendations for: {catalog[targetProductID]} ({targetProductID})")
    print("Rank | Product ID | Product Name       | Times Bought Together")
    print("-----|-------------|--------------------|----------------------")

    for index, (pid, count) in enumerate(recommendations, start=1):
        productname = catalog[pid]
        print(f"{index:<4}|{pid:<11}|{productname:<18}|{count}")

customerData = processTransactions(transactionLog)
frequentPairs = findFrequentPairs(customerData)
recommendations = getRecommendations('prod_10', frequentPairs)
generateReport('prod_10', recommendations, productCatalog)

