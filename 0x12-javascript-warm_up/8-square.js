#!/usr/bin/node
const times = process.argv;
const int_times = parseInt(times[2]);
if (isNaN(int_times)) {
	console.log('Missing size');
} else {
	for (let i = 0; i < int_times; i++) {
		let row = '';
		for (let j = 0; j < int_times; j++) {
			row += 'X';
		}
		console.log(row);
	}
}
