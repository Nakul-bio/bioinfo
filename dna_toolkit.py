dna = input("Enter a DNA sequence: ").upper()
valid_bases = {"A", "T" ,"C" ,"G"}
if all(bases in valid_bases for bases in dna):
    print("Valid dna Sequence")
else:
    print("Invalid DNA sequence")
    exit()
a_count = dna.count("A")
t_count = dna.count("T")
c_count = dna.count("C")
g_count = dna.count("G")

print("\nNucleotide counts: ")
print("A:" ,a_count)
print("T:" ,t_count)
print("C:" ,c_count)
print("G:" ,g_count)

gc_content = ((g_count+c_count)/len(dna))*100
print("\nGC content:")
print(f"{gc_content:.2f}%")

complement = {
    "A" : "T",
    "T" : "A",  
    "G" : "C",
    "C" : "G"
 }
reverse_complement = ""

for base in reversed(dna):
         reverse_complement += complement[base]   

   
print("\nReverse complement:")
print(reverse_complement)

rna=dna.replace("T","U")
print("\nRNA sequence:")
print(rna)

length = len(dna)
print("\nSequence length:")
print(length)

at_count = a_count + t_count
at_content = (at_count / len(dna)) * 100
print("\nAT content:")
print(f"{at_content:.2f}%")

print("\nStart Codon check:")
if dna.startswith("ATG"):
      print("start codon found!")
else:
     print("no start codon found.")


codon_table = {
    # Methionine (Start)
    "ATG": "M",

    # Phenylalanine
    "TTT": "F",
    "TTC": "F",

    # Leucine
    "TTA": "L",
    "TTG": "L",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",

    # Alanine
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",

    # Glycine
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",

    # Lysine
    "AAA": "K",
    "AAG": "K",

    # Stop codons
    "TAA": "*",
    "TAG": "*",
    "TGA": "*"
}
protein = ""
for i in range(0,len(dna)-2,3):
      codon = dna[i:i+3]
      if codon in codon_table:
        amino_acid = codon_table[codon]
        if amino_acid == "*":
            break
        protein += amino_acid
      else:
        protein += "X"
print("\nprotein_sequence:")
print(protein)           