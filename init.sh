cd merlin/tools
./compile_tools.sh
cd ../../
pip install -r merlin/requirements.txt
cd merlin/tools
tar -xvf speech_tools-2.4-release.tar.gz
cd speech_tools
./configure
make
cd ../
tar -xvf festival-2.4-release.tar.gz
tar -xvf festlex_CMU.tar.gz
tar -xvf festlex_OALD.tar.gz
tar -xvf festlex_POSLEX.tar.gz
tar -xvf festvox_kallpc16k.tar.gz
cd festival
./configure
make
cd ../
tar -xvf HTK-3.5.beta-2.tar.gz
cd htk/HTKLib
make -f MakefileCPU all
cd ../HTKTools
make -f MakefileCPU all
apt-get install sox
mkdir wav_files
cd wav_files
wget https://linksync-2032.kxcdn.com/wp-content/uploads/2017/06/female-voice-1.zip
unzip female-voice-1.zip
rm -rf female-voice-1.zip
cd ..
python preprocess.py
