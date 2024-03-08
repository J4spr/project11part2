# Met de lambda kun je bepalen welke waarde specifiek wordt gebruikt uit de lijst bv. lambda x: x.get('x') om de x uit
# de elementen in de lijst te gebruiken
# zoekt de hoogste waarde in de lijst
def getMax(value, lam):
    try:
        return max([lam(x) for x in value])
    except Exception as e:
        print(value)
        print(lam)
        print(f"\033[31m\033[1m[ERROR]: {e} in getMax()\033[0m")


# zoekt de laagste waarde in de lijst
def getMin(value, lam):
    try:
        return min([lam(x) for x in value])
    except Exception as e:
        print(f"\033[31m\033[1m[ERROR]: {e} in getMin()\033[0m")


# zoekt de meest voorkomende waarde in de lijst
def getMostFrequent(value, lam):
    try:
        list = []
        for i in value:
            list.append(lam(i))
        return max(set(list), key=list.count)
    except Exception as e:
        print(f"\033[31m\033[1m[ERROR]: {e} in getMostFrequent()\033[0m")


# zoekt de meest voorkomende waarde in de lijst die voldoet aan de criteria
def getMostFrequentlyWithCriteria(value, lam, criteria, criteriaLam):
    try:
        list = []
        for i in value:
            if criteriaLam(i) == criteria:
                list.append(lam(i))
        return max(set(list), key=list.count)
    except Exception as e:
        print(f"\033[31m\033[1m[ERROR]: {e} in getMostFrequentlyWithCriteria()\033[0m")


# zoekt het gemiddelde
def getAverage(value, lam, ):
    try:
        list = [lam(x) for x in value]
        return sum(list) / len(list)
    except Exception as e:
        print(f"\033[31m\033[1m[ERROR]: {e} in getMostFrequent()\033[0m")


# bepaald de som van de waardes in de lijst
def getSum(value, lam):
    try:
        list = []
        for i in value:
            try:
                list.append(lam(i))
            except:
                pass
        return sum(list)
    except Exception as e:
        print(f"\033[31m\033[1m[ERROR]: {e} in getMostFrequent()\033[0m")
