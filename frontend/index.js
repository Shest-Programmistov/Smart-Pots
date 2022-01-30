const express = require('express')
const fs = require('fs')
const { type } = require('os')
const path = require('path')
const app = express()

const ip = 'localhost'
const port = '3000'

app.use(express.static(path.join(__dirname, 'public')));
app.listen(port, () => {
    console.log(`App started at: http://${ip}:${port}`)
});