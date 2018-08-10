# https://leetcode.com/problems/number-of-matching-subsequences/description/
from collections import Counter

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.word = None
                self.is_leaf = True

            def add_children(self, c, child_node):
                self.children[c] = child_node
                self.is_leaf = False

        def buildTrie(word_list):
            root = TrieNode()
            # count = 0
            for word in word_list:
                node = root
                for c in word:
                    if c in node.children:
                        node = node.children[c]
                    else:
                        new_node = TrieNode()
                        # count += 1
                        node.add_children(c, new_node)
                        node = new_node
                node.word = word
            # print(count)
            return root

        counter = Counter(words)
        root = buildTrie(words)
        candidates = set([root])
        matched_word_set = set()
        for c in S:
            # print(len(candidates))
            for each_node in set(candidates):
                if c in each_node.children:
                    match_child = each_node.children[c]
                    if match_child.word:
                        matched_word_set.add(match_child.word)
                    if not match_child.is_leaf:
                        candidates.add(match_child)
        return sum(counter[word] for word in matched_word_set)

s = Solution()
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# S = "ricogwqznwxxcpueelcobbbkuvxxrvgyehsudccpsnuxpcqobtvwkuvsubiidjtccoqvuahijyefbpqhbejuisksutsowhufsygtwteiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoiundjscnlhbrhookmioxqighkxfugpeekgtdofwzemelpyjsdeeppapjoliqlhbrbghqjezzaxuwyrbczodtrhsvnaxhcjiyiphbglyolnswlvtlbmkrsurrcsgdzutwgjofowhryrubnxkahocqjzwwagqidjhwbunvlchojtbvnzdzqpvrazfcxtvhkruvuturdicnucvndigovkzrqiyastqpmfmuouycodvsyjajekhvyjyrydhxkdhffyytldcdlxqbaszbuxsacqwqnhrewhagldzhryzdmmrwnxhaqfezeeabuacyswollycgiowuuudrgzmwnxaezuqlsfvchjfloczlwbefksxsbanrektvibbwxnokzkhndmdhweyeycamjeplecewpnpbshhidnzwopdjuwbecarkgapyjfgmanuavzrxricbgagblomyseyvoeurekqjyljosvbneofjzxtaizjypbcxnbfeibrfjwyjqrisuybfxpvqywqjdlyznmojdhbeomyjqptltpugzceyzenflfnhrptuugyfsghluythksqhmxlmggtcbdddeoincygycdpehteiugqbptyqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmwwxzjckmaptilrbfpjxiarmwalhbdjiwbaknvcqovwcqiekzfskpbhgxpyomekqvzpqyirelpadooxjhsyxjkfqavbaoqqvvknqryhotjritrkvdveyapjfsfzenfpuazdrfdofhudqbfnzxnvpluwicurrtshyvevkriudayyysepzqfgqwhgobwyhxltligahroyshfndydvffd"
# words = ["iowuuudrgzmw","azfcxtvhkruvuturdicnucvndigovkzrq","ylmmo","maptilrbfpjxiarmwalhbd","oqvuahijyefbpqhbejuisksutsowhufsygtwteiqyligsnbqgl","ytldcdlxqbaszbuxsacqwqnhrewhagldzhr","zeeab","cqie","pvrazfcxtvhkruvuturdicnucvndigovkzrqiya","zxnvpluwicurrtshyvevkriudayyysepzq","wyhxltligahroyshfn","nhrewhagldzhryzdmmrwn","yqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmw","nhrptuugyfsghluythksqhmxlmggtcbdd","yligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoiundjsc","zdrfdofhudqbfnzxnvpluwicurrtshyvevkriudayyysepzq","ncygycdpehteiugqbptyqbvokpwovbnplshnzafun","gdzutwgjofowhryrubnxkahocqjzww","eppapjoliqlhbrbgh","qwhgobwyhxltligahroys","dzutwgjofowhryrubnxkah","rydhxkdhffyytldcdlxqbaszbuxs","tyqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmwwxzjc","khvyjyrydhxkdhffyytldcdlxqbasz","jajekhvyjyrydhxkdhffyytldcdlxqbaszbuxsacqwqn","ppapjoliqlhbrbghq","zmwwxzjckmaptilrbfpjxiarm","nxkahocqjzwwagqidjhwbunvlchoj","ybfxpvqywqjdlyznmojdhbeomyjqptltp","udrgzmwnxae","nqglnpjvwddvdlmjjyzmww","swlvtlbmkrsurrcsgdzutwgjofowhryrubn","hudqbfnzxnvpluwicurr","xaezuqlsfvchjf","tvibbwxnokzkhndmdhweyeycamjeplec","olnswlvtlbmkrsurrcsgdzu","qiyastqpmfmuouycodvsyjajekhvyjyrydhxkdhffyyt","eiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwyl","cgiowuuudrgzmwnxaezuqlsfvchjflocz","rxric","cygycdpehteiugqbptyqbvokpwovbnplshnzaf","g","surrcsgd","yzenflfnhrptuugyfsghluythksqh","gdzutwgjofowhryrubnxkahocqjzwwagqid","ddeoincygycdpeh","yznmojdhbeomyjqptltpugzceyzenflfnhrptuug","ejuisks","teiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoi","mrwnxhaqfezeeabuacyswollycgio","qfskkpfakjretogrokmxemjjbvgmmqrfdxlkfvycwalbdeumav","wjgjhlrpvhqozvvkifhftnfqcfjmmzhtxsoqbeduqmnpvimagq","ibxhtobuolmllbasaxlanjgalgmbjuxmqpadllryaobcucdeqc","ydlddogzvzttizzzjohfsenatvbpngarutztgdqczkzoenbxzv","rmsakibpprdrttycxglfgtjlifznnnlkgjqseguijfctrcahbb","pqquuarnoybphojyoyizhuyjfgwdlzcmkdbdqzatgmabhnpuyh","akposmzwykwrenlcrqwrrvsfqxzohrramdajwzlseguupjfzvd","vyldyqpvmnoemzeyxslcoysqfpvvotenkmehqvopynllvwhxzr","ysyskgrbolixwmffygycvgewxqnxvjsfefpmxrtsqsvpowoctw","oqjgumitldivceezxgoiwjgozfqcnkergctffspdxdbnmvjago","bpfgqhlkvevfazcmpdqakonkudniuobhqzypqlyocjdngltywn","ttucplgotbiceepzfxdebvluioeeitzmesmoxliuwqsftfmvlg","xhkklcwblyjmdyhfscmeffmmerxdioseybombzxjatkkltrvzq","qkvvbrgbzzfhzizulssaxupyqwniqradvkjivedckjrinrlxgi","itjudnlqncbspswkbcwldkwujlshwsgziontsobirsvskmjbrq","nmfgxfeqgqefxqivxtdrxeelsucufkhivijmzgioxioosmdpwx","ihygxkykuczvyokuveuchermxceexajilpkcxjjnwmdbwnxccl","etvcfbmadfxlprevjjnojxwonnnwjnamgrfwohgyhievupsdqd","ngskodiaxeswtqvjaqyulpedaqcchcuktfjlzyvddfeblnczmh","vnmntdvhaxqltluzwwwwrbpqwahebgtmhivtkadczpzabgcjzx","yjqqdvoxxxjbrccoaqqspqlsnxcnderaewsaqpkigtiqoqopth","wdytqvztzbdzffllbxexxughdvetajclynypnzaokqizfxqrjl","yvvwkphuzosvvntckxkmvuflrubigexkivyzzaimkxvqitpixo","lkdgtxmbgsenzmrlccmsunaezbausnsszryztfhjtezssttmsr","idyybesughzyzfdiibylnkkdeatqjjqqjbertrcactapbcarzb","ujiajnirancrfdvrfardygbcnzkqsvujkhcegdfibtcuxzbpds","jjtkmalhmrknaasskjnixzwjgvusbozslrribgazdhaylaxobj","nizuzttgartfxiwcsqchizlxvvnebqdtkmghtcyzjmgyzszwgi","egtvislckyltpfogtvfbtxbsssuwvjcduxjnjuvnqyiykvmrxl","ozvzwalcvaobxbicbwjrububyxlmfcokdxcrkvuehbnokkzala","azhukctuheiwghkalboxfnuofwopsrutamthzyzlzkrlsefwcz","yhvjjzsxlescylsnvmcxzcrrzgfhbsdsvdfcykwifzjcjjbmmu","tspdebnuhrgnmhhuplbzvpkkhfpeilbwkkbgfjiuwrdmkftphk","jvnbeqzaxecwxspuxhrngmvnkvulmgobvsnqyxdplrnnwfhfqq","bcbkgwpfmmqwmzjgmflichzhrjdjxbcescfijfztpxpxvbzjch","bdrkibtxygyicjcfnzigghdekmgoybvfwshxqnjlctcdkiunob","koctqrqvfftflwsvssnokdotgtxalgegscyeotcrvyywmzescq","boigqjvosgxpsnklxdjaxtrhqlyvanuvnpldmoknmzugnubfoa","jjtxbxyazxldpnbxzgslgguvgyevyliywihuqottxuyowrwfar","zqsacrwcysmkfbpzxoaszgqqsvqglnblmxhxtjqmnectaxntvb","izcakfitdhgujdborjuhtwubqcoppsgkqtqoqyswjfldsbfcct","rroiqffqzenlerchkvmjsbmoybisjafcdzgeppyhojoggdlpzq","xwjqfobmmqomhczwufwlesolvmbtvpdxejzslxrvnijhvevxmc","ccrubahioyaxuwzloyhqyluwoknxnydbedenrccljoydfxwaxy","jjoeiuncnvixvhhynaxbkmlurwxcpukredieqlilgkupminjaj","pdbsbjnrqzrbmewmdkqqhcpzielskcazuliiatmvhcaksrusae","nizbnxpqbzsihakkadsbtgxovyuebgtzvrvbowxllkzevktkuu","hklskdbopqjwdrefpgoxaoxzevpdaiubejuaxxbrhzbamdznrr","uccnuegvmkqtagudujuildlwefbyoywypakjrhiibrxdmsspjl","awinuyoppufjxgqvcddleqdhbkmolxqyvsqprnwcoehpturicf"]
S = "wngkwftovkvcqlxqprebdqwchzygbtbagcaawyamflmahcexxxdnroneecgxoobrfodlzfzhlyqcubmmkyjfswvezhudwdjbedisdjrkhxhrldiakgyawqrbtpjwopvyfvnswpskjihpwhbzlmimbpbecasyftcndybvkgolsrqgpizftloojgdxemtwiqxdccajiioleiotrilozthjbizsfahnphnqoyzeqokuabfkjcwhqxqzcwrltgwyjaazelahncrdmkdxpjjvhhsezhwtmxfpwoifzdzxqavptavspwrepchyterbesizdavjhwvwnhgyabhszgkddozggacpqnvvevjmqlgfsvgrsikdamhaarhdtqkrpxtmevxstqvggaoeysjhqquzdzfwodzytyexokaxjentudcxaqzasqkggwajhramcemtscknewhibkcwfgibyfsrnbpwgfmggnabhichuoqhwdlpsbxatonrgeuuixzrnbiqnkmoioazrahvpcbjhyqepasbxlwyfihdrmtypjyucbcjcdpkllwcnirsrsmzykbdmqrzavwkolnvmcsavwxnohqkutsfasgsoocofodlbjdtsotrnsvzqlaawwtsauhlvpiunubtgidzwldnqdregpbxnwoshspdpncqqflmnqodcddqetsyhspigoiktqlpgrrkovglutfrcinpdecavmgetzrlwozmboftrorelncsqpxhbryqumgliwzkmsxfksuwsjygrlurlgpwguteziytjbfnnzliawihprjolucsfctpyitwomsptjikoijqovevhmxokitapraodrpbvyyztzpdbypnzpbcedqjkahmwjcmorymebtaocxfecfbuuqqpdyqmdflsjijiyiqyelvvtucihakvfsxpzvmuuxdnvaaylihcdtrrmgvfkselvhbatuhnvnulykvtqkfgyasnabqbzxweihcfbvnrltt"
words = ["sptjikoijqovevhmxokitapraodrpb","raodrpbvyyztzpdbypnzpbcedqjkahmwj","ku","lncsqpxhbryqumgliwzkmsxfksuwsjygrlurlgpwguteziytjb","vwkolnvmcsavwxnohqkutsfasgs","tsotrnsvzqlaawwtsauh","repchyterbesizdavjhwvwnhgy","gpwguteziytjbfnnzliawihprjolucsfctpyitwomsptjik","ctpyitwomsptjikoijqovevhmxokit","d","kbd","gibyfsrnbpwgfmggnabhichuoqhwdlps","pvyfv","kmoioazrahvpcbjhyqepasbxlwyfihd","ecgxoobrfodl","rkhxhrldiakgyawqrbtpjwopvyfvnswpskjih","zavwkolnvmcsavwxnohqkuts","qlaawwt","atuhnvn","dybv","wvez","cofodlbjdtsotrnsvzqlaawwtsauhlvpiunubtgidzwldn","wjcmorymebtaocxfecfbuuqqpdyqmdflsjijiyiqyelvvt","npdecavmgetzrlwozmboftrorelncsqpxhbryqumgliwzkm","h","getzrlwozmboftro","gyabhszgkddozggacpqnvvevjmqlgfsvgrs","kolnvmcsavwxnohqkutsfasgsooc","mgetzrlwozmbo","xhbryqumgliwzkmsxfksuw","kwftovkvcqlxqprebd","ymebtaoc","wguteziytjbf","kddozggacpqnvvevjmqlg","zthjbizsfahnp","aaylihcdtrrmgvfkselvhbatuhnvnulykvtqkfgyasnabqbzxw","prjolucsfctpyitwomsptjikoijqovevhmxok","pbxnwoshspdpncq","atonrgeuuixzrnbiqnkmoioazrah","pjwopvyfvnswpskjihpwhbzlmim","pncqqflmnqodcddqetsyhspigoiktqlpgrr","tcndybvkgolsrqgpizftloojgdxemtwiqxdccajiioleiotr","hwvwnhgyabhszgkddozggacpqnvvevjmqlgfsvgrsik","nqoyze","khxhrl","urlgpwguteziytjbfnn","bfkjcwhqxqzcwrltgwyjaazelahncrdmkdxpjj","qlxqprebdqwchzygbtbagcaawyamflmahcex","dcxaqzasqkggwajhramcemtscknewhibkcwfgibyfsrnbpw","fnnzliawihprjolucs","qnonchqvlvbdlkobldjhzssahyqqmeykiewectwxtrhfsdtcxd","rpkpmddspdatshqgjtrztbebffuygwnzsrslxcgtkaazftefry","telhuriegkxetzewvunimgojtydbosfabrpetyjgthwpskbnks","nmrtgjrqpdmzrgxdogygilahebircujivfcgegbwkowjmhzilw","xfjedlhopwayrkzlptmlpytlnwrnantrhardwwastcvragmvcx","xzmluqjzqvrotixjardzzrmjasfstqdzhulxdnoknqcyamixsb","kdoevmbiljzkjtyuhwlkqbtiafpyqnfwjahukkihxhvrkvowrt","mjkpnrbxdixfrnvxlobeluevcehoyuulmeptyuocbfkfbsomlv","epwcotnebmvzdmaafjetathtkeqyqzqkaivwnqfpnxnqqtjvvi","ffysavcnflwczoilmmvehzlsdgzwklxlozbcemnoyzausavzdg","lafilmncpqfswvonhbgdafywplqhgwglrrovvmerrtdvbuvzfn","jhpeyjxdtjgyfaiorfzafxhrekhahwkginwcfjlpbxrevtskvj","jdsnvnrkwphpydqldqeozytkpimujaosylztugqnaxfimkhfqs","zqkwgqrfclrrekqwgotnizfaamfbowzhjlqwaqbbqwhshqycgd","kxvukzigjtntfugqrnxirxjrxjjsgbshkhblvfckhocwqmvmau","hecmosobfenbrfrgxvehewsgdgaglmftbuejhfbuvikvexbzsj","vilmdiatkodzcejdpgikcizkntcszhfoedcbohxbrwxmecwluo","gtglhyjlqprujdnqqstlufjqifejqmwidvicoldwohgfxoavdh","hhzrrvhohbbmekbxgsztqghvriudsiionobigachvmlmdwrdni","hwztpigfsyyeahphzdtkbnbmbodvpkaijijeftqjngtqvmtvby","gkxrsjtzxyynjiysqbsdlprjdgeaeroqfzjqciojgxcunudwmt","sgdfcuazxccskipfkxzyqergwgyekzeiqpnskqmiksbrrlrlfh","gvepdjmingnmnolubhnvfgdrupwoxdmoznydibvgmapzctccuw","kqyeapxbxpxjjwbnwdayuyfhrsyieyndeugdsmtqjsiyxeudgp","lnnnzvvnmdxwvoogcqpcjpalohywoosedxdzekauwiwpamfslk","fnxqvfrrmxrhjxjsotviphksjrmpihufwodldvqadkgvudiopd","prszelmhbuawewclunxtuxrkoembgxagwryyqmgizluuhlzmzq","vrlqtpkyezhgacdyqaeszudzfyxhzzxiryeveyzuxgmlgkeloj","frhpnzjhlvlbknewvutchdnbeursumndtqeazrczmudpixrqrg","sowyetlqbxscqechyqrxfejjmexztablsgsfqosayxylmnzfha","cqlrguoyemizmyqbvglxyqnytlhnagdkgjdtrekelkkzfemzyq","mmynrlrtnwokvrjquaeptmrmgtprjzkdliajtbvnrzynqozbmt","qotvsxsavfwzmobvfeywigacrujfgqdbctwvkhlriuolasmchf","kjiiaptxiypkzcdigsgooiohcqacweolkpdmkmowaolpaulccn","tiosaciyozvvmlhbgysjybdvuweitqqeavdaagxelvnodegbnf","acxegjvstpokvmozekztgqjbkwnylhkbrycnhnwaaacxrrgnvr","enufhwvogvravemymtlnmwbqjoyivxlsbdehruzjgdqpjobdaw","dquzygoznyrfgiotmxvcxygsfrplzrkktmzanbxmybbdnvaunf","irpqeotzlwlmybivmhwueopohpslnlfgbupoblardadqfbzywv","irwanlcdabjdvboszzgzaaxamsabsawnmaduycmkalkenhptzf","ttdiqzngjucxmdjcbocwyfjomkurkabmdgyqbzrkqsvzpjxddq","qbawfqazkttiejjcqrfhzbvzjhsqzgpjcdeqfhudvtzqvbzhdl","vqdhloonltowzqjeowmtkfwwnpdxuiopswmcclfaspknhlcbhu","ocpxihedbzzraxkrxluiqgqcviunankwrtgrmxhsfiaukgambd","eunuqntjekylkfuflvhnborregipgsagkcegwabsodwslxshwh","ceomxdvgwnjpbuwyapqwluncpzptfcvqcorfqmwmnwkmtioupv","drfwqpgqzqwdfgpdcmuvhkljsvjwjwtnjsdyuyoemrjsycoupq","hougyimwboycnqyfafejgqbvohcmawsqdkkbishqxgyfhoqdcm","xdrpvdulpraosijygaccuyimdvkgfxaupiljpfjmhljdrmjrah","lvtkcrqpzqjihutpeqschdpkoavvfcxlhgsjbxgqllgdkeimnr"]


print(s.numMatchingSubseq(S, words))

