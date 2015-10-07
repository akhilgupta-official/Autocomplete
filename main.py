import retrievalmain as rm
import probability as p
def main():
	x=raw_input("Enter the string : ")
	s = x.strip().split(" ",3)
	if len(s)>3:
		pw ,rel = rm.fourth_word(s[0],s[1],s[2],s[3])

		probable_word_list = p.probability_fourth_word(pw)
	if len(s)==3:
		fc,sc,rft,rst,pw,rel = rm.third_word(s[0],s[1],s[2])

		probable_word_list =  p.probability_third_word(fc,sc,rft,rst,pw)

	if len(s)==2:
		pw ,fwcount,rel=rm.second_word(s[0],s[1])
	
		#print "calling autocomplete"
		probable_word_list = p.probability_second_word(s[0],s[1],pw,fwcount)
	if len(s)==1 :
		probable_words = rm.first_word(s[0])
	
		#print "calling autocomplete"
		probable_word_list = p.probability_first_word(s[0],probable_words)
main()
