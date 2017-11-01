from heapq import *

def code(lowerLetter):
	binNum = "{0:b}".format(ord(lowerLetter)-97)
	pads = 5-len(binNum)
	pad = "0"*pads
	return pad+binNum

def runLength(message):
	#key = {'a':"00000", 'b':"00001", 'c':"00010", 'd':"00011", 'e':"00100", 'f':"00101", 'g':"00110", 'h':"00111", 'i':"01000", 'j':"01001", 'k':"01010", 'l':"01011", 'm':"01100", 'n':"01101", 'o':"01110", 'p':"01111", 'q':"10000", 'r':"10001", 's':"10010", 't':"10011", 'u':"10100", 'v':"10101", 'w':"10110", 'x':"10111", 'y':"11000", 'z':"11001"}
	encodedLength = 0
	previous = '?'

	for letter in message:
		if letter != previous:
			encodedLength = encodedLength + 24
			previous = letter
	
	return encodedLength

##############################################################################
# returns dictionary associating letter with length of letter's huffman code #
##############################################################################
def huffmanCodeLengths(heap):
	codeLengths = dict()
	offsets = dict()
	while len(heap) > 1:
		first = heappop(heap)
		second = heappop(heap)
		#print("first: "+str(first)+"\nsecond: "+str(second)+"\n")
		
		if len(first[1]) == 1:
			offsets[first[1]] = second[2]	
		if len(second[1]) == 1:
			offsets[second[1]] = first[2]	

		newHeight = max(first[2], second[2]) + 1
		newString = str(first[1]) + str(second[1])
		newFreq = first[0]+second[0]
		newNode = (newFreq, newString, newHeight)
		heappush(heap, newNode)
	
	heapHeight = heap[0][2]
	for letter in heap[0][1]:
		codeLengths[letter] = heapHeight - offsets[letter]

	return codeLengths

def huffman(message):
	freqs = dict()
	for i in range(ord('a'), ord('z')+1):
		freqs[chr(i)] = 0

	for letter in message:
		freqs[letter] = freqs[letter] + 1
	
	#heap will be composed of nodes represented as tuples with format (frequency, string, heightOfNode)
	heap = [(freqs[letter], letter, 0) for letter in freqs if freqs[letter] is not 0]
	if len(heap) == 1:
		return len(message)
	
	heapify(heap)
	codeLengths = huffmanCodeLengths(heap)	
	encodedLength = 0
	for letter in message:
		encodedLength = encodedLength + codeLengths[letter]

	return encodedLength

def main():
	inFile = open("input.txt", 'r')
	message = inFile.readline()
	inFile.close()
	
	message = message.strip('\n')
	outFile = open("output.txt", 'w')
	outFile.write(str(len(message)* 5)+"\n")
	outFile.write(str(runLength(message))+"\n")
	outFile.write(str(huffman(message))+"\n")
	outFile.close()


main()
