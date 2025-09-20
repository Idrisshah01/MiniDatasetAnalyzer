import csv 
def load_csv(file_path):
    """ it will read file and returns datat as a lists of dictionories"""
    try:
        with open(file_path,mode="r",encoding= "utf-8") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        print(f"Data Loaded successfully from {file_path}")
        return data
    except FileNotFoundError:
        print("File Not Found Please Cheake The Flie Path ")
        return []
    except Exception as e:
        print("Error Loading File : ", e)
        return []

def save_csv(file_path,data,fieldnames):
    try:
        with open(file_path,mode="w",encoding= "utf-8" , newline= "") as file:
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"data saved successfully to {file_path}")
    except Exception as e :
        print(" Error saving a file : ",e)