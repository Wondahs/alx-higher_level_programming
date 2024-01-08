#!/usr/bin/node
const times = process.argv;
const int_times = parseInt(times[2]);
if (isNaN(int_times)) {
	console.log('Missing number of occurrences');
} else {
	for (let i = 0; i < int_times; i++) {
		console.log('C is fun');
	}
}
