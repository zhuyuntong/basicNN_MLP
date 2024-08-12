from collections import Counter

s = 'abacadefghibj'
letters  = Counter(s.lower())

# total = 0
# nums_count = 0

# for letter in letters.most_common():
#     total+= letter[1] * (nums_count//9 + 1)
#     nums_count = nums_count+1


# print(total)

# def match_pattern(text, pat):
#     def matches(t, p):
        
#         prefix, suffix = p.split('*')
#         return t.startswith(prefix) and t.endswith(suffix) and len(t) >= len(prefix) + len(suffix)


#     return ["YES" if matches(t, p) else "NO" for t, p in zip(text,pat)]

# print(match_pattern('programming','r*in'))

p = 'r*in'
text = 'programming'

# p = 'ab*ef'
# text = 'abcdef'

p = 'ug*eb'
text = 'debug'

p = 'tzsxqtbplfnrzdwohcuv*kqnfurpubcmfljdhwmkwpq'
text = 'qdsukksqukmdlwwfdvyhmqoaavirmgcridfabnxfedkrinrkqbqtwcgfksyyhtounnjaqopgveocayohbyjmgrbxtvndwlbehovmgjqyqimwdlzfhpdgeohlamwxkykhieymaplrgrsmyqyqjpzcymyvwzaqrrpyeamfevnkkrgpeewccmogqlimmjzxutigypvladonpbwplayjvkqumhqjqydrgmidblmznhcmcapostcqwolpwvfovenerqvtnmeisjoznyfllvscrfdcjvvtjgistoobxwrglbzschnheqpmpzlknxxosvuzbxrgbgavorxxgvzclmwerainfrlnzbtsijbavpraqnibhfdskyaidlfvmnvczeueesfnhbmuuixsmafuhnybtzsxqtbplfnrzdwohcuvhbkqnfurpubcmfljdhwmkwpqltzsxqtbplfnrzdwohcuvkqnfurpubcmfljdhwmkwpqkqnfurpubcmfljdhwmkwpqkqnfurpubcmfljdhwmkwpqtzsxqtbplfnrzdwohcuvkqnfurpubcmfljdhwmkwpqtzsxqtbplfnrzdwohcuvfykqnfurpubcmfljdhwmkwpqzhtzsxqtbplfnrzdwohcuvutzsxqtbplfnrzdwohcuvtzsxqtbplfnrzdwohcuvtzsxqtbplfnrzdwohcuvfkqnfurpubcmfljdhwmkwpqstzsxqtbplfnrzdwohcuvlbtzsxqtbplfnrzdwohcuvibkqnfurpubcmfljdhwmkwpqkqnfurpubcmfljdhwmkwpqfkrkqnfurpubcmfljdhwmkwpqecltzsxqtbplfnrzdwohcuvlowztzsxqtbplfnrzdwohcuvbtzsxqtbplfnrzdwohcuvqtzsxqtbplfnrzdwohcuvnkqnfurpubcmfljdhwmkwpqtgkqnfurpubcmfljdhwmkwpqkqnfurpubcmfljdhwmkwpqkqnfurpubcmfljdhwmkwpqvqtzsxqtbplfnrzdwohcuvuvtfduglkwupbsmqrxzxlugbiykkgwjvfjtdvjjftzkcmytaoqznawamgliuswmyzerjsdrpvwjnwsemfjkdkefcspiplktcuidpuznltihomfmstmjjcfdkxspqhdciodbfibahhjnaxceoaftarrjogfhqifowmxpntlgnivyqrragelokmhcczhxdpadhjtpxnyoxayyeqiysjglrjduuomivnvfbbkwmkvlyttqqxtjwcziurlxsigkwkeducyzmjazgcbobnynjglfmyjsgbidtbfgpxocqizczytoisttvvyydazolilknkuafxyhnjliwtjnxersrouhhqznucfhibzvaaqnrgmawutcwkwglwegptwxhbuipieqwfzdubdhrrmlyjedllnqklqbytjjkjaukmebxcndqwmahvoedzxtceyyydzexiptxtsdyukdtjgcacdrvqaxpdekrgcnmaugtrngdnkqaymmkhrybpjlulkjwsyjvjkhwppmggoiebeepvcjofzywqwwsvsggqfmfvcqjgtbqnkmlcnayiwgvrmitkttunxrzpjhafrftwcnxofruloqqeubrlthjqpwoeftepyfiiaausalohkefzjthnrwfcnngrssrlbaocjaohbiskeewbftgnxajkhjsqnliprywjfmhnktksqkuzzcsqplanbcrnixojukgbttioppmkwkubdmnlywuzvwnnlybjavhrwyyrhyasgyqpbrbprwyelmwthqhdqmvxorbufgxaqjotnmprwnbguzlndsajzoktjzviburabbtzxowdtevuzbhbcpbexqfyrexqtppuesepjbnxngqfcmykmpjeompnpygaxbaotbscelgujjsxppgnjkfavduxmsucfswxyzmouvjgrtwjhnqybrlzjtzgmthdrgrbaijdvajenjfwgsnh'

prefix, suffix = p.split('*')

index1 = text.find(prefix)

if index1 == -1:
    print(-1)
else:
    index2 = text[index1 + len(prefix):].rfind(suffix)
    if index2 == -1:
        print(-1)
    elif index2 == 0 and suffix == '':
        print(len(text) - index1)
    else:
        index1 = index1 if index1 == 0 else index1-1
        print(index2 + len(suffix) + len(prefix) - index1)
# print(index1)