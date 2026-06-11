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
