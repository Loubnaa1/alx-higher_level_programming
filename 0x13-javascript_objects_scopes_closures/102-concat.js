#!/usr/bin/node
const files = require('fs');
const csfile0 = files.readFileSync(process.argv[0]);
const csfile1 = files.readFileSync(process.argv[1]);
files.writeFileSync(process.argv[2], csfile0 + csfile1);
