print("\t Menna Ayman Rashad \t")
print("\t Hello in Amino acid program \t")
print("*************************************************************")


names = {"TTT": "Phe(F)", "TTC": "Phe(F)", "TTA": "Leu(L)", "TTG": "Leu(L)", "TCT": "Ser(S)", "TCC": "Ser(S)", "TCA": "Ser(S)", "TCG": "Ser(S)", "TAT": "Tyr(Y)", "TAC": "Tyr(Y)", "TAA": "Stop", "TAG": "Stop", "TGT": "Cys(C)", "TGC": "Cys(C)", "TGA": "Stop", "TGG": "Trp(W)", "CTT": "leu(L)", "CTC": "leu(L)", "CTA": "leu(L)", "CTG": "leu(L)", "CCT": "Pro(P)", "CCC": "Pro(P)", "CCA": "Pro(P)", "CCG": "Pro(P)", "CAT": "His(H),His(H)", "CAC": "Gln(G)", "CAA": "Gln(G)", "CAG": "Arg(R)", "CGT": "Arg(R)", "CGC": "Arg(R)", "CGA": "Arg(R)", "CGG": "Ile(I)", "ATT": "Ile(I)", "ATC": "Ile(I)", "ATA": "Met(M)", "ATG": "Thr(T)", "ACT": "Thr(T)", "ACC": "Thr(T)", "ACA": "Thr(T)", "ACG": "Asn(N)", "AAT": "Asn(N)", "AAC": "Lys(K)", "AAA": "Lsy(K)", "AAG": "Ser(S)", "AGT": "Ser(S)", "AGC": "Ser(S)", "AGA": "Arg(R)", "AGG": "Arg(R)", "GTT": "Val(v)", "GTC": "Val(v)", "GTA": "Val(v)", "GTG": "Val(v)", "GCT": "Asp(D)", "GCC": "Asp(D)", "GCA": "Glu(E)", "GCG": "Glu(E)", "GAT": "Gly(G)", "GAC": "Gly(G)", "GGT": "Gly(G)", "GGC": "Gly(G)", "GGA": None, "GGG": None}


aminoname=input("Enter the name of amino acid: ")

if names[aminoname.upper()] is not None :
    print("The amino acid you entered is: [ {} ]".format(names[aminoname.upper()]))
else:
    print("Wrong Amino acid") 
    

 


        
