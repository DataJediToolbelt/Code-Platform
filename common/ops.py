import os

def  create_output_file(input_type: str, directory_name: str)->None:
    current_path = os.getcwd()
    current_output_path = current_path+"\\outputs\\"
    parent_path = os.path.normpath(current_path + os.sep + os.pardir)
    os.chdir(parent_path)
    def file_output_generation(input_type, sorted_list):
    # The check of the file existing is done before this in a seperate call currently
       try:
           if (input_type == "names_first"):
               output_file = "names_first.dat"
               for line_dtl in sorted_list:
                    datatier_id = str(line_dtl[0])
                    name_first = line_dtl[1]
                    gender_name = line_dtl[2]
                    dataattributeid = str(line_dtl[6])
                    application_guid = line_dtl[7]
                    #line_output = name_first,gender_name,dataattributeid,application_guid
                    # line_output ={datatier_id}+{name_first}
                    f = open(current_output_path+output_file, "a")
                    f.write(datatier_id+","+name_first+","+gender_name+","+dataattributeid+'\n')
                    f.close()
       except Exception as e:
                # If it fails, inform the user.
                print("Error in file outputting " % (output_file, e.strerror))

