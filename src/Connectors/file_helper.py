

def write_out_file(file_name: str, file_content: str):
    with open(file_name, "w") as file_out:
       file_out.write(file_content) 
