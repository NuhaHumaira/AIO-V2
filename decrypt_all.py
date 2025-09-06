import os

output_dir = "decrypted_files"
os.makedirs(output_dir, exist_ok=True)

def decrypt_file(in_file, out_file):
    if not os.path.exists(in_file):
        print(f"File not found: {in_file}")
        return
    with open(in_file,'r') as in_f, open(".temp1",'w') as temp_f:
        filedata = in_f.read()
        if "eval" not in filedata:
            print(f"Cannot decrypt (no eval found): {in_file}")
            return
        temp_f.write(filedata.replace("eval","echo"))
    os.system(f"bash .temp1 > .temp2")
    os.remove(".temp1")
    with open(".temp2",'r') as temp_f2, open(out_file,'w') as out_f:
        out_f.write("# Decrypted by K-fuscator\n\n"+temp_f2.read())
    os.remove(".temp2")
    print(f"Decrypted {in_file} → {out_file}")

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".sh"):
            full_path = os.path.join(root, file)
            out_path = os.path.join(output_dir, file.replace(".sh","_decrypted.sh"))
            decrypt_file(full_path, out_path)
