import os

def decrypt_file(in_file):
    if not os.path.exists(in_file):
        print(f"[!] File not found: {in_file}")
        return
    with open(in_file,'r') as in_f, open(".temp1",'w') as temp_f:
        filedata = in_f.read()
        if "eval" not in filedata:
            print(f"[!] Cannot decrypt (no eval found): {in_file}")
            return
        temp_f.write(filedata.replace("eval","echo"))
    os.system(f"bash .temp1 > .temp2")
    os.remove(".temp1")
    with open(in_file,'w') as out_f:  # overwrite original file with decrypted version
        out_f.write("# Decrypted by K-fuscator\n\n")
        with open(".temp2",'r') as temp_f2:
            out_f.write(temp_f2.read())
    os.remove(".temp2")
    print(f"[✓] Decrypted {in_file}")

# Walk through all directories
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".sh"):
            full_path = os.path.join(root, file)
            decrypt_file(full_path)
