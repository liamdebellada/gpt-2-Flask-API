var data = require('./filetocompile.json')
var fs = require('fs')

for (item in data) {
    console.log(item)
    fs.appendFile('output.txt', data[item].Text, (err) => {
        if (err) {
            console.log(err)
        }
    })
}

