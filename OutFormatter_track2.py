import csv
import time

#This class takes the output.txt file and coverts it to Mobility format
#C:\\postilion\\postcard\\data\\CardProduction_GHIPPS_Standard\\output.txt
class Openseseme2:
    def Open3(self):
        try:
            output_file = open('C:\\Temp\\output.txt')#open output.txt file
            timestr=time.strftime("%Y%m%d-%H%M%S")#allows you append date datetime to filename
            filename= 'output_ghipps_track2' + timestr +'.txt'#new outputfilename
            output_ghipps = open('C:\\Temp\\'+ filename,'w', newline='')#creates and open new file

            read_output = output_file.read().splitlines()  #read output.txt file

            total_number_of_records=len(read_output)#including header and trailer
            ary=[]
            i=1
            myparameters = ghipsformat()#calls the addons from the specs document
        
            while i < total_number_of_records-1:
                new_text=read_output[i].split(',')
                new_text = [myparameters.par1 + new_text[0] + myparameters.par2 + new_text[2] +new_text[20][21:24] +
                           myparameters.pvki + new_text[15] + new_text[12] + myparameters.zero + '?']
                ary.append(new_text)
                i=i + 1

        
            wr = csv.writer(output_ghipps,dialect='excel')
            for item in ary:
                wr.writerow(item)
                    
            output_file.close()
            output_ghipps.close()

            
        except FileNotFoundError:
            error_log= open("C:\\Temp\\errorlog.txt", "w+")
            error_log.write("Filenotfound:move output.txt  file to C:\postilion\postcard\data\CardProduction_GHIPPS_Standard ")
            error_log.close()



    
class ghipsformat:
    par1 = ';'
    par2='='
    pvki='0'
    zero='0'








