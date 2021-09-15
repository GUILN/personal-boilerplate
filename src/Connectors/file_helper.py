import os 

def write_out_file(file_name: str, file_content: str):
    try:
        with open(file_name, "w") as file_out:
            file_out.write(file_content) 
    except:
        os.makedirs(os.path.dirname(file_name)) 
        with open(file_name, "w") as file_out:
            file_out.write(file_content) 

def get_relative_path(actual_path: str, common_path:str) -> str: 
    print(f'actual path {os.path.dirname(actual_path)}')
    print(f'common path {os.path.dirname(common_path)}')
    #relative_path = os.path.relpath(os.path.abspath(actual_path), start=os.path.abspath(common_path))
    relative_path = actual_path.replace(common_path, '')
    return relative_path 
