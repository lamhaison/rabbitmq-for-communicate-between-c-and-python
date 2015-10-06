# rabbitmq-for-communicate-between-c-and-python
Using rabbitmq as message broker to communication betwen different language, c++ and python

The first step, please install rabbimq-server and turn it on. In the my lab, i using fedora 21 64bit		
yum install rabbitmq-server											
service rabbitmq-server start											
check status of rabbitmq-server										
service rabbitmq-server status											
Turn on it when start up machine										
chkconfig rabbitmq-server on											

The second step, we will buidl lib for rabbimq client dev and write simple demo using c++ interact with rabbitmq

BUILD LIBRARY FOR DEV IN C++
Install Dependency
yum install boost-devel
sudo yum install openssl-devel
Install rabbitqm-c
wget https://codeload.github.com/alanxz/rabbitmq-c/tar.gz/v0.7.0
tar xzvf rabbitmq-c-0.7.0.tar.gz
cd rabbitmq-c-0.7.0
mkdir build
cd build
cmake ..
sudo cmake --build . --config Release --target install
Install SimpleAmqpClient
cd ~/Downloads/
wget https://github.com/alanxz/SimpleAmqpClient/archive/master.zip
unzip master.z
cd SimpleAmqpClient-master/
mkdir simpleamqpclient-build
cd simpleamqpclient-build
cmake ..
make
make install

Build Source
cd SimpleAmqpClient-master/examples

change source: 
from #include <SimpleAmqpClient.h> to #include <SimpleAmqpClient/SimpleAmqpClient.h>
export export LD_LIBRARY_PATH=/usr/local/lib
	

compile: g++ -W -Wall -Wextra -pedantic -lSimpleAmqpClient -std=c++11 simple_connect.cpp

using for python, this is very simple
only just install pika lib. execute command line
pip install pika

REF 
https://github.com/alanxz/rabbitmq-c
https://github.com/alanxz/SimpleAmqpClient
https://www.rabbitmq.com/devtools.html

Run demo
please read Describe about simple demo file to understand my demo

Thank your for watching!
