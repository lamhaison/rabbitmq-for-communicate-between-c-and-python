nclude <SimpleAmqpClient/SimpleAmqpClient.h>

#include <iostream>
#include <stdlib.h>

using namespace AmqpClient;
int main()
{
    char *szBroker = getenv("AMQP_BROKER");
    Channel::ptr_t channel;
    if (szBroker != NULL)
        channel = Channel::Create(szBroker);
    else
        channel = Channel::Create();

    channel->DeclareQueue("alanqueue");
    channel->BindQueue("alanqueue", "amq.direct", "alankey");

    BasicMessage::ptr_t msg_in = BasicMessage::Create();

    msg_in->Body("asdfghjkl");

    //channel->BasicPublish("amq.direct", "alankey", msg_in);

    channel->BasicConsume("alanqueue", "consumertag");
    BasicMessage::ptr_t msg_out = channel->BasicConsumeMessage("consumertag")->Message();

    std::cout << "Message text: " << msg_out->Body() << std::endl;

}

