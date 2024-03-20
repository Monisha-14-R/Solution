def virusIndices(p,v):
    def is_matching(sub_p,sub_v):
        if len(sub_p) != len(sub_v):
            return False
        mismatch_count = 0
        for i in range(len(sub_p)):
            if sub_p[i] != sub_v[i]:
                mismatch_count += 1
                if mismatch_count > 1:
                    return False
        return True
    matches = []
    for i in range(len(p) - len(v) + 1):
        sub_p = p[i:i+len(v)]
        if is_matching(sub_p,v):
            matches.append(str(i))
    if matches:
       return''.join(matches)
    else:
        return "No Match!"
test_case0 = [("abbab","ba"),
              ("hello","world"),
              ("banana","nan")]
for p,v in test_case0:
    res = (virusIndices(p,v))
    if res != "No Match!":
        print(res)
    else:
        print(res)


test_case1 = [("cgatcg","gc"),
              ("atcgatcga","cgg"),
              ("aardvark","ab")]
for p,v in test_case1:
    res = (virusIndices(p, v))
    if res != "No Match!":
        print(res)
    else:
        print(res)















