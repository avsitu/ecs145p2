def calcfreqs(infile,nqs=None,maxrat=None):
	f = open(infile)
	lines = f.readlines()
	lines[len(lines)-1] = lines[len(lines)-1]+'\n'
	freqs = {}
	for l in lines:
		tmp = l[:-1].replace('NA','X').replace(' ','')
		if tmp in freqs:
			freqs[tmp]+=1
		else:
			freqs[tmp] = 1		
	return freqs

def highfreqs(freqs,k):
	sorted_freqs = sorted(freqs.items(), key=lambda t:t[1], reverse=True)	
	tmp = filter(lambda t:t[1]>=sorted_freqs[k-1][1], sorted_freqs)	
	return list(tmp)

freqs = calcfreqs('testfile.txt')
print (highfreqs(freqs, 2))