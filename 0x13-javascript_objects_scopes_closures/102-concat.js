#!/usr/bin/node
const files = require('fs');
const csfile0 = files.readFileSync(process.argv[1]);
const csfile1 = files.readFileSync(process.argv[2]);
files.writeFileSync(process.argv[3], csfile0 + csfile1);
