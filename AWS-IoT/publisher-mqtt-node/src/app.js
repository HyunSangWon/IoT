const awsIot = require("aws-iot-device-sdk");

const device = awsIot.device({
    keyPath: "YOUR_KEY",
    certPath: "YOUR_CERT",
    caPath: "YOUR_CA",
    clientId: "YOUR_CLIENTID",
    host: "YOUR_HOST",
});

const data = {
    temperature: 38,
    humidity: 80,
    barometer: 1013,
    wind: {
        velocity: 22,
        bearing: 255,
    },
};

device.on("connect", () => {
    console.log("connect");
    device.publish("device/99/data", JSON.stringify(data));
});

device.on("message", (topic, payload) => {
    console.log("message", topic, payload.toString());
});
