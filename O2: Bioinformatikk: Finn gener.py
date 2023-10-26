genes = []
gene_start = -1

genome_input = input("Enter a genome string ")

for i in range(len(genome_input)):
    if genome_input[i:i+3] == "ATG":
        gene_start = i
    elif genome_input[i:i+3] in ["TAG", "TAA", "TGA"] and gene_start != -1:
        gene_end = i
        genes.append(genome_input[gene_start+3:gene_end])
        gene_start = -1

if genes:
    for gene in genes:
        print(gene)
else:
    print("No genes found")