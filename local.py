#!/usr/local/bin/python3
# cut strings into exons and introns
with open("plain_genomic_seq.txt") as my_file:
     contents=my_file.read()
     intron=contents[:64] 
     second_exon=contents[92:] 
     first_exon=contents[65:91]
# replacing bad letters 
     intron=intron.replace("X","A").replace("t","T").replace("K","C").replace("S","G")
# writing files
with open("intron.fasta", "w") as intron1:
     intron1.write(intron)
with open("exon2.fasta", "w") as exon2:
     exon2.write(second_exon)
with open("exon1.fasta", "w") as exon1:
     exon1.write(first_exon)
with open("coding.fasta","w") as code:
     code.write(first_exon+second_exon)