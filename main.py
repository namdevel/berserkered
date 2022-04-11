'''
Deobfuscate python code obfuscated by Berserker
Author : namdevel (https://github.com/namdevel/berserkered)
'''
import os, sys, re
import subprocess
  
def write(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    f.close()


if __name__ == "__main__":

    obf_file = "obfuscated.py"  # obfuscated file

    with open(obf_file) as code:
        data = code.read()
        
        s1 = re.search("if self.(.+?) in open", data).group(1)
        s1s = s1.replace("15", "12")
        s2 = re.findall("{(.+?)}", data)

        source = (
            data.replace(s1, s1s)
            .replace("{" + s2[0] + "}", "print")
            .replace(",{" + s2[1] + "}()", "")
        )
        write('tmpfile.py', source)
        subprocess.run(f"py tmpfile.py") # show real code in terminal
        os.unlink('tmpfile.py')