import os
import sys

if __name__ == "__main__":

    in_file_path = sys.argv[1]
    out_file_path = sys.argv[2]
    
    if os.path.exists(out_file_path):
        os.remove(out_file_path)

    with open(in_file_path, 'r') as in_file:  
        with open(out_file_path, 'w') as out_file:
            for line in in_file.readlines():
                name, label = line.split()
                face_id = name.split('_')[-1]
                dir = name[:-len(face_id)-1]
                out_file.write("{}\t{}\n".format(os.path.join(dir, name), label))