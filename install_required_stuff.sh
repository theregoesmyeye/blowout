pkg install clang python libffi openssl libsodium 
SODIUM_INSTALL=system pip install pynacl 
pip install paramiko 
git clone https://github.com/zacheller/rockyou 
cd rockyou 
tar xvf rockyou.txt.tar.gz 
mv rockyou.txt .. 
rm -rf rockyou 
echo "Wordlist has been added. Thanks to https://github.com/zacheller for providing the mirror."
