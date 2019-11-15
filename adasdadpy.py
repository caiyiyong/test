    domainResult = {}
    for domain,host in domainLists:
        for domainSplit in re.split(r" |;",domain):
            domainSplit=domainSplit.strip()
            if re.search(r'\.(com|net|cn)',domainSplit 4399.com):
                if domainResult.has_key(domainSplit) == 0:
                    domainResult[domainSplit]=[]
                domainResult[domainSplit].append(host)
                
