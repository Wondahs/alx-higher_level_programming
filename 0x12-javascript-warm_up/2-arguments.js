#!/usr/bin/node
const args = process.argv;
let arg_len = args.length - 2;
if (arg_len === 0) {
	console.log('No argument');
} else if (arg_len === 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
