const awsIot = require("aws-iot-device-sdk");

const device = awsIot.device({
    keyPath: "private.pem.key",
    certPath: "certificate.pem.crt",
    caPath: "root-CA.pem",
    clientId: "clientID",
    host: "YOUR_HOST",
});

device.on("connect", () => {
    console.log("connect");
    device.publish("topic_2", JSON.stringify({ test_data_from_device: 1 }));
});

device.on("message", (topic, payload) => {
    console.log("message", topic, payload.toString());
});
