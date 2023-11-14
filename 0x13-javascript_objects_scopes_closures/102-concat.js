#!/usr/bin/node
const files = require('fs');
const csfile0 = files.readFileSync(process.argv[2]);
const csfile1 = files.readFileSync(process.argv[3]);
files.writeFileSync(process.argv[4], csfile0 + csfile1);
