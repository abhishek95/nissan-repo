import 
'''

hostname = 'm11.cloudmqtt.com'
port = 14037
clientid = 'api'
var client = new Messaging.Client(hostname, port, clientid);

var options = {
 
     //connection attempt timeout in seconds
     timeout: 3,
 
     //Gets Called if the connection has successfully been established
     onSuccess: function () {
         alert("Connected");
     },
 
     //Gets Called if the connection could not be established
     onFailure: function (message) {
         alert("Connection failed: " + message.errorMessage);
     }
 
 };
 
client.connect(options);
'''