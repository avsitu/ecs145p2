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
	items = freqs.items()
	unique_freqs = set(map(lambda t:t[1],items))
	if abs(k) > len(unique_freqs):
		return freqs	
	sorted_freqs = sorted(unique_freqs)
	
	tmp = []
	if k > 0:
		tmp = list(filter(lambda t:t[1]>=sorted_freqs[k-1], items))
	elif k < 0:
		tmp = list(filter(lambda t:t[1]<=sorted_freqs[k], items))
	d = {}
	for t in tmp:
		d[t[0]] = t[1]			
	return d

freqs = calcfreqs('testfile')
print freqs
print highfreqs(freqs, 2)
print highfreqs(freqs, -2)