document.addEventListener('WebComponentsReady', function() {
    startButton.addEventListener('click', function () {

        const currentValues = {
            index_finger: null,
            middle_finger: null
        }

        const getValue = event => event.target.value.getUint8(0);

        const updateValues = type => event => {
            currentValues[type] = getValue(event)
            updateHtml()
            fetch(engine_host + '/glove', {
                method: 'POST',
                headers: {
                  'Access-Control-Allow-Origin': '*',
                  'content-type': 'application/json'

                },
                body: JSON.stringify(currentValues)
            })
            // .then(console.log)
            .catch(console.error)
        }

        navigator.bluetooth.requestDevice({ filters: [{ services: ['33332a58-0000-1000-8000-00805f9b34ff'] }] })
        .then(device => device.gatt.connect())
        .then(server => server.getPrimaryService('33332a58-0000-1000-8000-00805f9b34ff'))
        .then(async service => {
            const index_finger = await service.getCharacteristic('33332a58-0000-1000-8000-00805f9b34aa')
            await index_finger.startNotifications()
            index_finger.addEventListener('characteristicvaluechanged', updateValues('index_finger'));

            const middle_finger = await service.getCharacteristic('33332a58-0000-1000-8000-00805f9b34bb')
            await middle_finger.startNotifications()
            middle_finger.addEventListener('characteristicvaluechanged', updateValues('middle_finger'));

        })
        .catch(error => { console.log(error); });

        function updateHtml() {
          document.getElementById('sensor-values').innerText = `Sensor: ${currentValues.index_finger} ${currentValues.middle_finger}`;
          console.log(`Sensor; index_finger:${currentValues.index_finger}, middle_finger: ${currentValues.middle_finger}`);
          // TODO: Parse Heart Rate Measurement value.
          // See https://github.com/WebBluetoothCG/demos/blob/gh-pages/heart-rate-sensor/heartRateSensor.js
        }
    });
});
